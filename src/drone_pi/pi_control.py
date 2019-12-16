""" This file is used to take controller input
    and return a value to control the drone.
    This will eventually be the file controlling the drone.
    MORE FUCTIONALITY WILL BE ADDED LATER."""

camera_mode = False # Used for switching between camera control and drone control
camera_toggle = 0 # Used to control camera without having to hold the button
camera_lock = False # Used due to a glitch with input control
camera_feed = False # Used for switching on and off camera feed
camera_feed_toggle = 0 # Used to control camera feed without having to hold the button
camera_feed_lock = False # Used due to a glitch with input control
drone_off = False # Used to turn drone off

def use_input(inputs):
    global camera_mode
    global camera_toggle
    global camera_lock
    global camera_feed
    global camera_feed_toggle
    global camera_feed_lock
    global drone_off
 
    if 'BTN_START' in inputs: # Start Button
        if inputs['BTN_START'] == 1:
            drone_off = True
            return 'TURNING DRONE OFF'
    elif 'BTN_WEST' in inputs: # Y Button, used for camera toggle
        if inputs['BTN_WEST'] == 1:
            camera_lock = False
            if camera_toggle % 2 == 0:
                camera_mode = True
                return 'CAMERA MODE ON'
            elif camera_toggle % 2 != 0:
                camera_mode = False
                return 'CAMERA MODE OFF'
        elif inputs['BTN_WEST'] == 0:
            if camera_lock == False:
                camera_toggle += 1
                camera_lock = True
            elif camera_lock == True:
                pass
            pass
    elif 'BTN_SOUTH' in inputs: # A Button, used for camera feed
        if inputs['BTN_SOUTH'] == 1:
            camera_feed_lock = False
            if camera_feed_toggle % 2 == 0:
                camera_feed = True
                return 'CAMERA FEED ON'
            elif camera_feed_toggle % 2 != 0:
                camera_feed = False
                return 'CAMERA FEED OFF'
        elif inputs['BTN_SOUTH'] == 0:
            if camera_feed_lock == False:
                camera_feed_toggle += 1
                camera_feed_lock = True
            elif camera_feed_lock == True:
                pass
            pass
    elif 'ABS_X' in inputs: # Left stick X movement
        if inputs['ABS_X'] < 0: # X Left movement (DELETE THIS WHEN PUTTING IN INPUTS)
            return f'MOVING LEFT STICK LEFT: {inputs["ABS_X"]}'
        elif inputs['ABS_X'] > 3000: # X Right movement (DELETE THIS WHEN PUTTING IN INPUTS)
            return f'MOVING LEFT STICK RIGHT: {inputs["ABS_X"]}'
        else:
            return f'LEFT STICK X NEUTRAL: {inputs["ABS_X"]}' # X Neutral (DELETE THIS WHEN PUTTING IN INPUTS)
    elif 'ABS_Y' in inputs: # Left stick Y movement
        if inputs['ABS_Y'] < -1500: # Y Up movement (DELETE THIS WHEN PUTTING IN INPUTS)
            return f'MOVING LEFT STICK UP: {inputs["ABS_Y"]}'
        elif inputs['ABS_Y'] > 1500: # Y Down movement (DELETE THIS WHEN PUTTING IN INPUTS)
            return f'MOVING LEFT STICK DOWN: {inputs["ABS_Y"]}'
        else:
            return f'LEFT STICK Y NEUTRAL: {inputs["ABS_Y"]}' # Y Neutral (DELETE THIS WHEN PUTTING IN INPUTS)
    elif 'ABS_RX' in inputs: # Right stick X movement
        if inputs['ABS_RX'] < 0: # RIGHT X Left movement (DELETE THIS WHEN PUTTING IN INPUTS)
            return f'MOVING RIGHT STICK LEFT: {inputs["ABS_RX"]}'
        elif inputs['ABS_RX'] > 3000: # RIGHT X Right movement (DELETE THIS WHEN PUTTING IN INPUTS)
            return f'MOVING RIGHT STICK RIGHT: {inputs["ABS_RX"]}'
        else:
            return f'LEFT RIGHT X NEUTRAL: {inputs["ABS_RX"]}' # RIGHT X Neutral (DELETE THIS WHEN PUTTING IN INPUTS)
    elif 'ABS_RY' in inputs: # Right stick Y movement
        if inputs['ABS_RY'] < -1500: # RIGHT Y Up movement (DELETE THIS WHEN PUTTING IN INPUTS)
            return f'MOVING RIGHT STICK UP: {inputs["ABS_RY"]}'
        elif inputs['ABS_RY'] > 1500: # RIGHT Y Down movement (DELETE THIS WHEN PUTTING IN INPUTS)
            return f'MOVING RIGHT STICK DOWN: {inputs["ABS_RY"]}'
        else:
            return f'RIGHT STICK Y NEUTRAL: {inputs["ABS_RY"]}' # RIGHT Y Neutral (DELETE THIS WHEN PUTTING IN INPUTS)
