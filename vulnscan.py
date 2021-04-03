
#!/usr/bin/python

import socket
import  os  # used to check whether the file exist or not
import sys # in order to check the no of arguements in the program



def retbanner(ip,port):
        try:
                socket.setdefaulttimeout(2)
                s=socket.socket()
                s.connect((ip,port))
                banner=s.recv(1024)
                return  banner
        except:
                return



def checkvulns(banner,filename):
	f=open(filename,'r')
	for line in f.readlines():
		if line.strip('/n') in banner:
			print 'server is vulnerable' + banner.strip('/n')

def main():
	if len(sys.argv)==2:
		filename=sys.argv[1] # keeping it on the second place on the no of arguements
		if not os.path.isfile(filename):
			print '[-] file doesnot exist'
			exit(0)
		if not os.access(filename,os.R_OK):
			print '[-] Access denied'
			exit(0)
	else:
		print 'Usage'+str(sys.argv[0])+'<vuln filename>'
		exit(0)
	portlist=[21,22,25,80,110,443,445]
	for x in range(4,6):
		ip='192.168.10.'+str(x)
		for port in portlist:
			banner=retbanner(ip,port)
			if banner:
				print ip +'/' + str(port)+ ':'+ banner
				checkvulns(banner,filename)

main()
