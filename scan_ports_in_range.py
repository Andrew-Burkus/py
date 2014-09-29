import optparse
import socket 
from socket import *

#check connection
def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send('Don\'t worry I\'m just messing around\r\n')

		#ping server
		results = connSkt.recv(100)
		print '[+]%d/tcp open'% tgtPort
		print '[+] ' + str(results)

		#close connection
		connSkt.close()

	except:
		'[-]%d/tcp closed'% tgtPort

#scan ports
def portScan(tgtHost, maxPort):
	try:
		#convert to IP
		tgtIP = gethostbyname(tgtHost)

	except:
		print "[-] Cannot resolve '%s': Unknown host"%tgtHost
		return

	try:
		tgtName = gethostbyaddr(tgtIP)
		print '[+] Scan Results for: ' + tgtName[0]

	except:
		print '\n[+] Scan Results for: ' + tgtIP + '\n'

	setdefaulttimeout(1)

	for tgtPort in range(0, maxPort):
		connScan(tgtHost, tgtPort)
		#print 'Scanning port ' + str(tgtPort)
		
#main
def main():
	#parse options from CLI
	parser = optparse.OptionParser('usage %prog -H' + \
		'<target host>')

	parser.add_option('-H', dest='tgtHost', type='string', \
		help='specify target host')

	parser.add_option('-p', dest='maxPort', type='int', \
		help='specify maximum port to scan')
	(options, args) = parser.parse_args()

	tgtHost = options.tgtHost
	maxPort = options.maxPort

	if(tgtHost == None) | (maxPort == None):
		print parser.usage
		exit(0)

	portScan(tgtHost, maxPort)

if __name__ == '__main__':
	main()
