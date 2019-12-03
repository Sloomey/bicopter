import socket # Used for sending data wirelessly
#import RPi.GPIO as GPIO, USED LATER
import time # Used for time

listensocket = socket.socket() # Makes a socket on IPV4 using TCP
PORT = 8080 # Port to host server on
maxConnections = 5 # Max connections to host at a time
IP = socket.gethostname() # IP address of local machine

listensocket.bind(('',PORT))

listensocket.listen(maxConnections) # Starts server
print(f'Server started at {IP} on port {PORT}')

clientsocket, address = listensocket.accept() # Accepts the incomming connection
print(f'Connection from {address} has been established!')

while True:
    message = clientsocket.recv(1024).decode("utf-8") #Gets the incomming message
    print(message)
