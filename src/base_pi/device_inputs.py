""" This file is used to gather all the inputs from the user's device. REMINDER: REMOVE ALL 'time.sleep's WHEN ADDING FUCTIONALITY."""

from switchcase import switch # Implements switch cases in python
import keyboard # Implements keyboard input in python
import mouse # Implements mouse input in python
import time # Implements functions using time in python

stop_program = False # Stops the program and drone 

keyboard_buttons = ['w', 'a', 's', 'd', 'f' , 'g', 'h', 'j', 'k', 'q'] # List of all buttons on keyboard being used

""" Function used to see what input the user is doing and if the input
    isn't a listed input it won't do anything. """
def device_input(controller_used = False, keyboard_used = False):
    global stop_program
    if keyboard_used == True:
        for count, button in enumerate(keyboard_buttons):
            for case in switch(count):
                if case(0): # W Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        time.sleep(0.05)
                        """ Later function will be added later. """
                elif case(1): # A Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        time.sleep(0.05)
                        """ Later function will be added later. """
                elif case(2): # S Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        time.sleep(0.05)
                        """ Later function will be added later. """
                elif case(3): # D Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        time.sleep(0.05)
                        """ Later function will be added later. """
                elif case(4): # F Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        time.sleep(0.05)
                        """ Later function will be added later. """
                elif case(5): # G Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        time.sleep(0.05)
                        """ Later function will be added later. """
                elif case(6): # H Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        time.sleep(0.05)
                        """ Later function will be added later. """
                elif case(7): # J Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        time.sleep(0.05)
                        """ Later function will be added later. """
                elif case(8): # K Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        time.sleep(0.05)
                        """ Later function will be added later. """
                elif case(9): # Q Key
                    if keyboard.is_pressed(button):
                        print('Exiting...')
                        stop_program = True
                else:
                    pass

        previous_mouse = mouse.get_position()
        time.sleep(0.005)
        current_mouse = mouse.get_position() 
        if current_mouse[0] > previous_mouse[0]: # Checks if the current mouse position X is greater than the previous mouse position X (going right)
            print('Mouse is moving right...')
            time.sleep(0.5)
            """ Later function will be added later. """
        elif current_mouse[0] < previous_mouse[0]: # Checks if the current mouse position X is less than the previous mouse position X (going left)
            print('Mouse is moving left...')
            time.sleep(0.5)
            """ Later function will be added later. """
        if current_mouse[1] > previous_mouse[1]: # Checks if the current mouse position Y is greater than the previous mouse position Y (going down)
            print('Mouse is moving down...')
            time.sleep(0.5)
            """ Later function will be added later. """
        elif current_mouse[1] < previous_mouse[1]: # Checks if the current mouse position Y is less than the previous mouse position Y (going up)
            print('Mouse is moving up...')
            time.sleep(0.5)
            """ Later function will be added later. """
            
    elif controller_used == True:
        print('Controller input coming soon.')
        stop_program = True
    else:
        print("Please Choose an input device. This can be achieved by typing 'controller_used = True' or 'keyboard_used = True' in the function's parameters.")
        stop_program = True

if __name__ == '__main__': # Only runs this code if you execute this file.
    while not stop_program:  
        try:
            device_input(keyboard_used = True)
        except Exception as error:
            print(error)
            print('ERROR: EXITING')
            break
