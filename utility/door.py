import time
from pymata4 import pymata4

def open_door():
    num_steps = 1024
    pins = [8,9,10,11]
    board = pymata4.Pymata4()

    board.set_pin_mode_stepper(num_steps, pins)

    board.stepper_write(21, num_steps)

    # time.sleep(10)
    # board.stepper_write(21, 1024)

def close_door():
    num_steps = 1024
    pins = [8,9,10,11]
    board = pymata4.Pymata4()

    board.set_pin_mode_stepper(num_steps, pins)

    board.stepper_write(21, 1024)

