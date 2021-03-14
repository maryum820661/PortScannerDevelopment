# !/usr/bin/python

from socket import *
import optparse
# This library help us to specify the help options  prompted to the user

from threading import *
def connScan(tgthost,tgtport):
	try:
		sock= socket(AF_INET,SOCK_STREAM)
		sock.connect((tgthost,tgtport))
		print('[+] %d /tcp Open' % tgtport)
	except:
		print('[-] %d /tcp Closed' % tgtport)
	finally:
		sock.close()

def portscan(tgthost,tgtports):
	#resolving the hostname
	try:
		tgtIP= gethostbyname(tgthost)
	except:
		print ('Unknown Host %s' %tgthost)
	try:
		tgtName=gethostbyaddr(tgtIP)
		print('[+] Scan Results for' + tgtName[0])
	except:
		print('[+] Scan Results for' + tgtIP)
	setdefaulttimeout(1)
	for tgtport in tgtports:
		t=Thread(target=connScan,args=(tgthost,int(tgtport)))
		t.start()
def main():
	parser=optparse.OptionParser('Usage of Program ' + '-H <targethost> -p <targetport>')
	parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
	parser.add_option('-p',dest='tgtport',type='string',help='specify target port seperated by comma ')
	(options,args)=parser.parse_args()
	tgthost=options.tgtHost
	tgtports=str(options.tgtport).split(',')
	if(tgthost== None) | (tgtports[0]==None):
		print(parser.usage)
		exit(0)
	portscan(tgthost,tgtports)

if __name__== '__main__':
	main()
	


