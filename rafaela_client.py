#!/usr/bin/env python3
# API for Rafaela The Cute Robot
# 
# Sid (2020)

import serial
import atexit

class Rover():
    def __init__(self, device='/dev/rfcomm0', bitrate=9600, debug=False):
        self.comm = serial.Serial(device, bitrate)
        self.debug = debug
        atexit.register(self.exit_handler)

    def exit_handler(self):
        print('Exiting...')
        print('Back to initial position....')
        self.move_stop()
        self.face_forward()
        print('Closing communication channel...')
        self.comm.close()
        print('OK')

    def send_cmd(self, cmd, param=None):
        if param is not None:
            cmd = cmd + ' ' + str(param)
        cmd = cmd + '\r\n'
        if self.debug: print(cmd)
        self.comm.write(bytes(cmd.encode('UTF-8')))
    
    def receive_info(self):
        return self.comm.readline().decode('UTF-8').rstrip()

    def move_motor(self, motor, speed=255):
        if speed > 255:
            speed = 255
        elif speed < -255:
            speed = 255
        if motor == 'LEFT':
            self.send_cmd('l', speed)
        elif motor == 'RIGHT':
            self.send_cmd('r', speed)

    def move_stop(self):
        self.move_motor('LEFT', 0)
        self.move_motor('RIGHT', 0)
    
    def move_forward(self,speed=255):
        self.move_motor('LEFT',speed)
        self.move_motor('RIGHT',speed)

    def move_backward(self, speed=255):
        self.move_motor('LEFT', -1*speed)
        self.move_motor('RIGHT', -1*speed)

    def rotate(self, speed=255):
        self.move_motor('LEFT', -1*speed)
        self.move_motor('RIGHT', speed)

    def face(self, angle):
        self.send_cmd('s', angle)

    def face_left(self):
        self.face(90)

    def face_right(self):
        self.face(-90)

    def face_forward(self):
        self.face(-10)

    def get_distance(self):
        self.send_cmd('p')
        return int(self.receive_info())

    def get_accel(self):
        self.send_cmd('a')
        accel_dt = self.receive_info().split(',')
        return list(map(float, accel_dt))

    def get_time(self):
        self.send_cmd('t')
        return self.receive_info()

    def disconnect(self):
        self.comm.close()

if __name__ == '__main__':
    import time
    rafaela = Rover()
    rafaela.move_stop()
    rafaela.disconnect()
    #test()
