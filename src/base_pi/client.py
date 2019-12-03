""" This file is used to send the input to the drone wirelessly.
    MAKE SURE YOUR RASPBERRY PI IS NAMED "raspberrypi" OR IT WON'T WORK."""

import socket # Used for sending data wirelessly
import device_inputs as di # Used for input

keyboard = False
mouse = False
controller = False


while True: #Loop gets the input used
    input_used = input('Keyboard or controller (WARNING: KEYBOARD IS UNSTABLE CURRENTLY): ').lower()
    if input_used == 'keyboard':
        keyboard = True
        while True:
            input_used = input('Mouse? (yes/no): ')
            if input_used == 'yes':
                mouse = True
                break
            elif input_used == 'no':
                mouse = False
                break
            else:
                print('Please type "yes" or "no"')
                continue
        break
    elif input_used == 'controller':
        controller = True
        break
    else:
        print('Please type "keyboard" or "controller"')
        continue
s = socket.socket() # Makes a socket on IPV4 using TCP

hostname = 'raspberrypi' # Server IP/Hostname 
PORT = 8080 # Server Port

s.connect((hostname, PORT)) #Connects to server

while True:
    input_message = di.device_input(controller, keyboard, mouse)
    if input_message == None:
        pass
    else:
        s.send(input_message.encode("utf-8")) #Encodes and sends message
