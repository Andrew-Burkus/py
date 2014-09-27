import ftplib

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
	