#!/usr/bin/python

import socket

from termcolor import colored
#Creating the socket object

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.setdefaulttimeout(1)
#This socket.AF_INET basically stands for IPV4 address and this socket.SOCK_STREAM  means that we will be using the TCP packets for  scanning

host=input("[*] Enter the Host to Scan:")
#if sock.connect_ex retreives an error then  show that the  specified port is closed and will respond close.


def portscanner(port):
        if sock.connect_ex((host,port)):
                print (colored("Port %d  is closed" % (port),'red'))
        else:
                print (colored("Port %d is opened" % (port),'green'))

for port in range(1,1000):
	portscanner(port)



