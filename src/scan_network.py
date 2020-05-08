from scapy.all import *
from scapy.layers.inet import IP, ICMP


def send_icmp_packet(target):
    _packet = IP(dst=target[0], ttl=10)/ICMP()
    reply = sr1(_packet, timeout=2, verbose=False)

    print(reply)

    # print(target, reply)
    if reply is not None:
        print(target[0] + ' is up')
