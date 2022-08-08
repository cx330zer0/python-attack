import socket
import optparse


def banneracq(host,port):
	try:
		conn = socket.socket()
		conn.connect((host,port))
		res = conn.recv(4096)
		print str(res)
		conn.close()
	except:
		pass



def main():
	parser = optparse.OptionParser('usage%prog '+'-H <target host> -P <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-P', dest='tgtPort', type='int', help='specify target port')
	(options, args) = parser.parse_args()
	host = options.tgtHost
	port = options.tgtPort
	if (host == None) | (port == None):
		print parser.usage
		exit(0)
	banneracq(host,port)


if __name__ == '__main__':
	main()

