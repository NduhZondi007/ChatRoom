import socket
import sys
import time

host = new_socket = socket.socket() #create a socket. #'ANALOGY: create the bridge'
hostname = socket.gethostname() #get host name of current device
socket_ip = socket.gethostbyname(hostname) #retrieves the ip of the other user which is stored in the variable basically 'client ip address'
port = 50148

# Binding the host and port name
new_socket.bind((hostname, port))
print('Binding successfull...')
print("This is your ip:", socket_ip)

# listenting for TCP connections
name = input("Enter your nickname: ")
new_socket.listen(1) # is there anyone try to connect to my server.

#accept incoming connections
conn, add = new_socket.accept() # 'conn - connected to the socket, add - ip address of the client'

print("Received connection from " + add[0])
print("connection Established. Connected from: " + add[0])

# storing connection data
client = (conn.recv(1024)).decode() #details of the incoming connection are stored in the client variable
print(client + " has connected.")
conn.send(name.encode()) # send host name to the client

# delivering messages
while True: 
    messages = input("Me : ")
    conn.send(message.encode()) # i will be sending the message now.
    message = conn.recv(1024) # receive incoming message
    message = message.decode()
    print(client + " : " + message)