# Client.py
# Send a file to server
# 2021 - 03 -31

import socket  # Import Modules
import sys

sock = socket.socket()  # Assign sock variable "socket.socket()" for ease of use
sock.connect(("192.168.0.36", 5000))  # Connect to server machine on port 5000
greetings = (
    "Hello from " + socket.gethostname()
)  # Assign variable text to send to other machine

sock.send(greetings.encode())  # Send text to print on Server's CLI
file = open("/home/matt/cronscript/output.txt", "rb")  # Open desired file to be sent

info = file.read(1024)  # Reads file's lines
print("Sending file...")  # Tell user file is being sent
while info:
    sock.send(info)  # Loops and keeps sending till finished
    info = file.read(1024)
print("\nFinished sending file.")


sock.close()  # Close connection

print("\nConnection closed.")
