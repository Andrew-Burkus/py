import ftplib
import socket
import optparse
from socket import *

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'me@your.com')

		print '\n[*] ' + str(hostname) + \
			' FTP Anonymous Login Succeeded.'
		ftp.quit()
		return True

	except Exception, e:
		print '\n[-] ' + str(hostname) + \
			' FTP Anonymous Login Failed.'
		return False

def getIP(host):
	try:
		#convert to IP
		tgtIP = gethostbyname(host)
		return tgtIP
	except:
		print "[-] Cannot resolve '%s': Unknown host"%host
		return
	
def main():
	parser = optparse.OptionParser('usage%prog ' + \
		'-H <target host>')
	parser.add_option('-H', dest='tgtHost', type='string', \
		help='specify target host')

	(options, args) = parser.parse_args()

	tgtHost = options.tgtHost

	if (tgtHost == None):
		print parser.usage
		exit(0)

	tgtIP = getIP(tgtHost)

	anonLogin(tgtIP)

if __name__ == '__main__':
	main()