import socket
import sys
import time

# Creating the socket and accepting user input

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
port =  50148

# Connection the server
print("This your IP address: " + ip)
server_host = input("Enter your friend's ip address: ")
name = input("Enter friend's name: ")
socket_server.connect((server_host, port))

# Receiving messages from the server
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, 'has joined...')

while True: 
    message = (socket_server.recv(1024)).decode()
    print(server_name + " : " + message)
    message = input("Me : ")
    socket_server.send(message.encode())
