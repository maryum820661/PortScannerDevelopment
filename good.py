#!/usr/bin/python
#receive bytes  from the ports which could be the version of the software on which they are running

import socket 


def retbanner(ip,port):
        try:
                socket.setdefaulttimeout(2) #setting the default time for the socket
                s=socket.socket() #making an object of the socket.
                s.connect((ip,port)) # connect to the target
                banner=s.recv(1024) # we want to receive 1024 bytes from the port.
                return banner
        except:
                return 

def main():
	ip=raw_input('Enter the IP address')
        for port in range(1,100): #port for ssh.Explicitly open port
        	banner=retbanner(ip,port)
      	        if banner:
               		 print '[+]'+ ip + '/ '+str(port) + ':' + banner.strip('/n')


main()

