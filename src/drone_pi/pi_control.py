""" This file is used to take controller input
    and return a value to control the drone.
    This will eventually be the file controlling the drone.
    MORE FUCTIONALITY WILL BE ADDED LATER."""

def use_input(inputs): 
    if 'BTN_TL' in inputs: # Left Bumper
        return {
            1: 'PRESSING LEFT BUMPER' ,
            0: 'RELEASING LEFT BUMPER',
        }[inputs['BTN_TL']]
    elif 'BTN_TR' in inputs: # Right Bumper
        return {
            1: 'PRESSING RIGHT BUMPER' ,
            0: 'RELEASING RIGT BUMPER',
        }[inputs['BTN_TR']]
