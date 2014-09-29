from scapy.all import *
import optparse

def pktPrint(pkt):
	if pkt.haslayer(Dot11Beacon):
		print '[+] Detected 802.11 Beacon Frame'
	elif pkt.haslayer(TCP):
		print '[+] Detected a TCP Packet'
	elif pkt.haslayer(DNS):
		print '[+] Detected a DNS Packet'

conf.iface = 'mon0'
sniff(prn = pktPrint)

#if __name__ == '__main__':
#	main()