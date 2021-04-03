  GNU nano 4.9.3                                                                retbanner.py                                                                Modified  
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
        port=22 #port for ssh.Explicitly open port
        ip='192.168.10.4'
        banner=retbanner(ip,port)
        if banner:
                print '[+]'+ ip + ':' + banner


main()



