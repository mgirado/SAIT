# Server.py
# Receive a file from client
# 2021 - 03 - 31

import socket  # Import Modules
import sys


filename = input(
    "\nDesired filename for file being received, leave empty for default: "
)  # Ask user for desired filename, leave empty for a predefined filename

if filename == "":
    filename = "virus.txt"
else:  # if else condition to see if user assigned a filename or left it empty
    filename = filename + ".txt"

print("\nFile will be called: " + filename)  # Print to CLI what filename will be called
sock = socket.socket()  # Assign variable for ease of use
sock.bind(("0.0.0.0", 5000))  # What address to listen to and which port

sock.listen(
    5
)  # Listens and waits for a connection, the integer is the max backlog number

print("Waiting for connection...\n")

connection, address = sock.accept()  # Accept connection

file = open(filename, "wb")  # Open file

while True:

    info = connection.recv(1024)
    print(
        "Receiving data from: " + str(address[1])
    )  # IP Address we're receiving data from
    print("\nClient: " + info.decode())  # Prints what client sent
    print("\nReceiving file...\n")
    byte_counter = 0
    while (
        info
    ):  # Loop counts number of bytes and also takes info to be put into file being received.
        file.write(info)
        info = connection.recv(1024)
        print("Bytes received: ", byte_counter)
        byte_counter += 1024
    break

file.close()  # Close file
print("\nFinished receiving file")

total_kb = byte_counter / 1024
print("\nTotal file size: " + str(total_kb) + " KB")

sock.close()
print("\nConnection closed.")
