""" This file is used to gather all the inputs from the user's device. REMINDER: REMOVE ALL 'time.sleep's WHEN ADDING FUCTIONALITY."""

from switchcase import switch # Implements switch cases in python
import keyboard # Implements keyboard input in python
import mouse # Implements mouse input in python
import inputs # Implements controller input for python
import time # Implements functions using time in python

stop_program = False # Stops the program and drone 

keyboard_buttons = ['w', 'a', 's', 'd', 'f' , 'g', 'h', 'j', 'k', 'q'] # List of all buttons on keyboard being used
mouse_buttons = ['left', 'middle', 'right'] # List of all mouse buttons being used

""" List of all controller buttons used. First index in tuple is the name of the button,
    second index is the actual button name known by the library,
    third index is the number the library uses to know when it's being pressed. This has been setup for an xbox controller. """

controller_buttons = [('RIGHT BUMPER', 'BTN_TR', 1), ('LEFT BUMPER', 'BTN_TL', 1),
                      ('DPAD-UP', 'ABS_HAT0Y' , -1), ('DPAD-DOWN', 'ABS_HAT0Y', 1), ('DPAD-RIGHT', 'ABS_HAT0X', 1), ('DPAD-LEFT', 'ABS_HAT0X', -1),
                      ('START BUTTON', 'BTN_START', 1), ('SELECT BUTTON', 'BTN_SELECT', 1),
                      ('X-BUTTON', 'BTN_NORTH', 1), ('Y-BUTTON', 'BTN_WEST', 1), ('B-BUTTON', 'BTN_EAST', 1), ('A-BUTTON', 'BTN_SOUTH', 1),
                      ('LEFT TRIGGER', 'ABS_Z', 1023), ('RIGHT TRIGGER', 'ABS_RZ', 1023)] 

""" Function used to see what input the user is doing and if the input
    isn't a listed input it won't do anything. """
def device_input(controller_used = False, keyboard_used = False, mouse_used = False):
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
            
    elif controller_used == True:
        events = inputs.get_gamepad() # Gets input from controller
        for event in events:
            for count, button in enumerate(controller_buttons):
                for case in switch(count):
                    if case(0): #Right Bumper
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    elif case(1): #Left Bumper
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    elif case(2): #DPAD UP
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    elif case(3): #DPAD DOWN
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    elif case(4): #DPAD RIGHT
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    elif case(5): #DPAD LEFT
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    elif case(6): #START BUTTON
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    elif case(7): #SELECT BUTTON
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    elif case(8): #X BUTTON
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    elif case(9): #Y BUTTON
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    elif case(10): #B BUTTON
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    elif case(11): #A BUTTON
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    elif case(12): # LEFT TRIGGER
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    elif case(13): # RIGHT TRIGGER
                        if event.code == button[1] and event.state == button[2]:
                            print('Pressing {}...'.format(button[0]))
                            """ Later function will be added later. """
                    else:
                        pass
                    
                
            
    else:
        print("Please Choose an input device. This can be achieved by typing 'controller_used = True' or 'keyboard_used = True' in the function's parameters.")
        stop_program = True

    if mouse_used == True:
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
        for count, button in enumerate(mouse_buttons):
            for case in switch(count):
                if case(0): # Left mouse button
                    if mouse.is_pressed(button=button):
                        print('Pressing {} mouse button...'.format(button))
                        time.sleep(0.05)
                        """ Later function will be added later. """
                elif case(1): # Middle mouse button (wheel)
                    if mouse.is_pressed(button=button):
                        print('Pressing {} mouse button...'.format(button))
                        time.sleep(0.05)
                        """ Later function will be added later. """
                elif case(2): # Right mouse button 
                    if mouse.is_pressed(button=button):
                        print('Pressing {} mouse button...'.format(button))
                        time.sleep(0.05)
                        """ Later function will be added later. """
                else:
                    pass

if __name__ == '__main__': # Only runs this code if you execute this file.
    while not stop_program:  
        try:
            device_input(controller_used = True)
        except Exception as error:
            print(error)
            print('ERROR: EXITING')
            break
