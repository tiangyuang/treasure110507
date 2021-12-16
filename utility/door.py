import time

from pymata4 import pymata4



def door():
    board = pymata4.Pymata4()
    num_steps = 1024
    pins = [8,9,10,11]

    board.set_pin_mode_stepper(num_steps, pins)
    board.stepper_write(21, num_steps)

