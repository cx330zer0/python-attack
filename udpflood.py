

from scapy.all import *



def udpconn(packet):
	sendp(packet)








eth = Ether()
ip = IP()
ip.dst = '172.16.1.200'
udp = UDP()
udp.dport = 53








m = 0
while True:
	packet = eth/ip/udp
	udpconn(packet)
	print('Sending Packet To %s '%ip.dst + 'Port Is %s'%udp.dport)
	m = m + 1
	print(m)
	



