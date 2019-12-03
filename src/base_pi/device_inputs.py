""" This file is used to gather all the inputs from the user's device. REMINDER: REMOVE ALL 'time.sleep's WHEN ADDING FUCTIONALITY."""

from switchcase import switch # Implements switch cases in python
import keyboard # Implements keyboard input in python
import mouse # Implements mouse input in python
import inputs # Implements controller input for python
import time # Implements functions using time in python

stop_program = False # Stops the program and drone

dpad_left = False # Used to fix bug with DPAD
dpad_down = False # Used to fix bug with DPAD

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
    global dpad_left
    global dpad_down
    
    if keyboard_used == True:
        for count, button in enumerate(keyboard_buttons):
            for case in switch(count):
                if case(0): # W Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        return "WK"
                elif case(1): # A Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        return "AK"
                elif case(2): # S Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        return "SK"
                elif case(3): # D Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        return "DK"
                elif case(4): # F Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        return "FK"
                elif case(5): # G Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        return "GK"
                elif case(6): # H Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        return "HK"
                elif case(7): # J Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        return "JK"
                elif case(8): # K Key
                    if keyboard.is_pressed(button):
                        print('Pressing {} key...'.format(button))
                        return "KK"
                elif case(9): # Q Key
                    if keyboard.is_pressed(button):
                        print('Exiting...')
                        stop_program = True
                        return "QK"
                else:
                    pass
            
    elif controller_used == True:
        events = inputs.get_gamepad() # Gets input from controller
        for event in events:
            for count, button in enumerate(controller_buttons):
                for case in switch(count):
                    if case(0): 
                        if event.code == button[1] and event.state == button[2]: # RIGHT BUMPER PRESSED
                            print('Pressing {}...'.format(button[0]))
                            return "RB "
                        elif event.code == button[1] and not event.state == button[2]: # RIGHT BUMPER UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            return "R0 "
                    elif case(1):
                        if event.code == button[1] and event.state == button[2]: # LEFT BUMPER PRESSED
                            print('Pressing {}...'.format(button[0]))
                            return "LB "
                        elif event.code == button[1] and not event.state == button[2]: # LEFT BUMPER UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            return "L0 "
                    elif case(2):
                        if event.code == button[1] and event.state == button[2]: # DPAD UP PRESSED
                            print('Pressing {}...'.format(button[0]))
                            return "DU "
                        elif event.code == button[1] and event.state == 0 and dpad_down == False: # DPAD UP UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            return "0U "
                    elif case(3):
                        if event.code == button[1] and event.state == button[2]: # DPAD DOWN PRESSED
                            print('Pressing {}...'.format(button[0]))
                            dpad_down = True
                            return "DD "
                        elif event.code == button[1] and event.state == 0 and dpad_down == True: # DPAD DOWN UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            dpad_down = False
                            return "0D "
                    elif case(4):
                        if event.code == button[1] and event.state == button[2]: # DPAD RIGHT PRESSED
                            print('Pressing {}...'.format(button[0]))
                            return "DR "
                        elif event.code == button[1] and event.state == 0 and dpad_left == False: # DPAD RIGHT UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            return "0R "
                    elif case(5):
                        if event.code == button[1] and event.state == button[2]: # DPAD LEFT PRESSED
                            print('Pressing {}...'.format(button[0]))
                            dpad_left = True
                            return "DL "
                        elif event.code == button[1] and event.state == 0 and dpad_left == True: # DPAD LEFT UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            dpad_left = False
                            return "0L "
                    elif case(6):
                        if event.code == button[1] and event.state == button[2]: # START BUTTON PRESSED
                            print('Pressing {}...'.format(button[0]))
                            return "S1 "
                        elif event.code == button[1] and not event.state == button[2]: # START BUTTON UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            return "01 "
                    elif case(7):
                        if event.code == button[1] and event.state == button[2]: # SELECT BUTTON PRESSED
                            print('Pressing {}...'.format(button[0]))
                            return "S2 "
                        elif event.code == button[1] and not event.state == button[2]: # SELECT BUTTON UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            return "02 "
                    elif case(8):
                        if event.code == button[1] and event.state == button[2]: # X BUTTON PRESSED
                            print('Pressing {}...'.format(button[0]))
                            return "XB "
                        elif event.code == button[1] and not event.state == button[2]: # X BUTTON UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            return "X0 "
                    elif case(9):
                        if event.code == button[1] and event.state == button[2]: # Y BUTTON PRESSED
                            print('Pressing {}...'.format(button[0]))
                            return "YB "
                        elif event.code == button[1] and not event.state == button[2]: # Y BUTTON UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            return "Y0 "
                    elif case(10):
                        if event.code == button[1] and event.state == button[2]: # B BUTTON PRESSED
                            print('Pressing {}...'.format(button[0]))
                            return "BB "
                        elif event.code == button[1] and not event.state == button[2]: # B BUTTON UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            return "B0 "
                    elif case(11):
                        if event.code == button[1] and event.state == button[2]: # A BUTTON PRESSED
                            print('Pressing {}...'.format(button[0]))
                            return "AB "
                        elif event.code == button[1] and not event.state == button[2]: # A BUTTON UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            return "A0 "
                    elif case(12):
                        if event.code == button[1] and event.state == button[2]: # LEFT TRIGGER PRESSED
                            print('Pressing {}...'.format(button[0]))
                            return "LT "
                        elif event.code == button[1] and event.state == 0: # LEFT TRIGGER UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            return "T0 "
                    elif case(13):
                        if event.code == button[1] and event.state == button[2]: # RIGHT TRIGGER PRESSED
                            print('Pressing {}...'.format(button[0]))
                            return "RT "
                        elif event.code == button[1] and event.state == 0: # RIGHT TRIGGER UNPRESSED
                            print('Letting go of {}...'.format(button[0]))
                            return "0T "
                    else:
                        pass

        if event.code == 'ABS_Y': # Left stick Y movement, UP = NEGATIVE AND DOWN = POSTIVE
            print('Moving left stick up/down...')
            return('LY: ' + str(event.state) + ' ')
        if event.code == 'ABS_X': # Left stick X movement, LEFT = NEGATIVE AND RIGHT = POSTIVE
            print('Moving left stick right/left...')
            return('LX: ' + str(event.state) + ' ')
        if event.code == 'ABS_RY': # Right stick Y movement, UP = NEGATIVE AND DOWN = POSTIVE
            print('Moving right stick up/down...')
            return('RY: ' + str(event.state) + ' ')
        if event.code == 'ABS_RX': # Right stick X movement, LEFT = NEGATIVE AND RIGHT = POSTIVE
            print('Moving right stick right/left...')
            return('RX: ' + str(event.state) + ' ')
                    
                
            
    else:
        print("Please Choose an input device. This can be achieved by typing 'controller_used = True' or 'keyboard_used = True' in the function's parameters.")
        stop_program = True

    if mouse_used == True:
        previous_mouse = mouse.get_position()
        time.sleep(0.005)
        current_mouse = mouse.get_position() 
        if current_mouse[0] > previous_mouse[0]: # Checks if the current mouse position X is greater than the previous mouse position X (going right)
            print('Mouse is moving right...')
            return "MR"
        elif current_mouse[0] < previous_mouse[0]: # Checks if the current mouse position X is less than the previous mouse position X (going left)
            print('Mouse is moving left...')
            return "ML"
        if current_mouse[1] > previous_mouse[1]: # Checks if the current mouse position Y is greater than the previous mouse position Y (going down)
            print('Mouse is moving down...')
            return "MD"
        elif current_mouse[1] < previous_mouse[1]: # Checks if the current mouse position Y is less than the previous mouse position Y (going up)
            print('Mouse is moving up...')
            return "MU"
        for count, button in enumerate(mouse_buttons):
            for case in switch(count):
                if case(0): # Left mouse button
                    if mouse.is_pressed(button=button):
                        print('Pressing {} mouse button...'.format(button))
                        return "LM"
                elif case(1): # Middle mouse button (wheel)
                    if mouse.is_pressed(button=button):
                        print('Pressing {} mouse button...'.format(button))
                        return "MM"
                elif case(2): # Right mouse button 
                    if mouse.is_pressed(button=button):
                        print('Pressing {} mouse button...'.format(button))
                        return "RM"
                else:
                    pass

if __name__ == '__main__': # Only runs this code if you execute this file.
    while not stop_program:  
        try:
            print(device_input(controller_used = True))
        except Exception as error:
            print(error)
            print('ERROR: EXITING')
            break
