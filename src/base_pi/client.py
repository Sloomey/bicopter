""" This file is used to send the input to the drone wirelessly.
    MAKE SURE YOUR RASPBERRY PI IS NAMED "raspberrypi" OR IT WON'T WORK."""

import socket # Used for sending data wirelessly
import json # Used to encode python objects
from inputs import get_gamepad # Used for controller input

def controller_input(): # Used for getting controller inputs
        events = get_gamepad()
        for event in events:
            return (event.code, event.state)

if __name__ == "__main__":
    s = socket.socket() # Makes a socket on IPV4 using TCP

    hostname = 'raspberrypi' # Server IP/Hostname 
    PORT = 31415 # Server Port

    s.connect((hostname, PORT)) #Connects to server

    while True:
        controller_inputs = controller_input()
        controller_pressed = {controller_inputs[0]: controller_inputs[1]}
        msg = json.dumps(controller_pressed) # Encodes message
        print(msg) # Used for debugging
        try:
                s.send(msg.encode('utf-8')) # Sends message  
        except ConnectionResetError:
                print('Drone has disconnected')
                break
                
    
