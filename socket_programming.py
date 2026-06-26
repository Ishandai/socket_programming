#sockets
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 7777

S=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Af_INET is the address family for IPv4. SOCK_STREAM means connection oriented TCP protocol
S.connect((HOST, PORT))