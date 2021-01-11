#!/usr/bin/python

import socket
#Creating the socket object

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.setdefaulttimeout(2)
#This socket.AF_INET basically stands for IPV4 address and this socket.SOCK_STREAM  means that we will be using the TCP packets for  scanning

host=raw_input("[*] Enter the Host to Scan:")
port=int(raw_input("[*] Enter the Port to Scan:"))
#if sock.connect_ex retreives an error then  show that the  specified port is closed and will respond close.


def portscanner(port):
	if sock.connect_ex((host,port)):
		print "Port %d  is closed" % (port)
	else:
		print "Port %d is opened" % (port)

portscanner(port)
