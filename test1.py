#!/usr/bin/env python3

import tkinter
from rafaela_client import Rover
import time

rafaela = Rover()
speed = 0
headangle = 0
rotatespeed = 0
rotate = False

def keypress(event):
    global speed
    global headangle
    global rotatespeed
    global rotate
    key = event.char

    if key == 'w':
        speed += 64
        if speed > 255:
            speed = 255
    elif key == 's':
        speed -= 64
        if speed < -255:
            speed = -255
    elif key == 'a':
        rotate = True
        rotatespeed = 255
    elif key == 'd':
        rotate = True
        rotatespeed = -255
    elif key == 'j':
        headangle += 15
        if headangle > 90:
            headangle = 90
    elif key == 'k':
        headangle -= 15
        if headangle < -90:
            headangle = -90


root = tkinter.Tk()
root.title('Shitty Control')

def action():
    global rotate
    if rotate:
        rafaela.rotate(rotatespeed)
        rotate = False
    else:
        rafaela.face(headangle)
        rafaela.move_motor('RIGHT', speed)
        rafaela.move_motor('LEFT', speed)
    root.after(10, action)

root.after(10, action)
root.bind('<Key>', keypress)
tkinter.mainloop()
