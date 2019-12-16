import socket # Used for sending data wirelessly
import json # Used to decode python objects
import pi_control # Used to control drone
import time # Used for time

listensocket = socket.socket() # Makes a socket on IPV4 using TCP
PORT = 31415 # Port to host server on
maxConnections = 1 # Max connections to host at a time
IP = socket.gethostname() # IP address of local machine

listensocket.bind(('',PORT))

listensocket.listen(maxConnections) # Starts server
print(f'Server started at {IP} on port {PORT}')

clientsocket, address = listensocket.accept() # Accepts the incomming connection
print(f'Connection from {address} has been established!')

while pi_control.drone_off == False:
    try:
        controller_inputs = clientsocket.recv(1024).decode('utf-8') #Gets the incomming message
        msg = json.loads(controller_inputs)
        if pi_control.use_input(msg) == None:
            pass
        else:
            print(pi_control.use_input(msg))
    except json.decoder.JSONDecodeError:
        pass

listensocket.shutdown(socket.SHUT_RDWR) # Shuts down socket
listensocket.close() # Closes Socket
print(f'Closing server at {IP} on port {PORT}')
