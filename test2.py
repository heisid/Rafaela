#!/usr/bin/env python3

import tkinter
from rafaela_client import Rover
import time

rafaela = Rover()

def keypress(event):
    key = event.char
    if key == 'w':
        rafaela.move_forward()
    elif key == 's':
        rafaela.move_stop()
    elif key == 'a':
        rafaela.rotate(255)
    elif key == 'd':
        rafaela.rotate(-255)
    elif key == 'z':
        rafaela.face_left()
    elif key == 'c':
        rafaela.face_right()
    elif key == 'x':
        rafaela.face_forward()

root = tkinter.Tk()

root.bind('<Key>', keypress)
tkinter.mainloop()
