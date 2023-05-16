#!/usr/bin/python

import socket
import socks

from scapy.all import * 

# Creates SOCKS5 socket
sock = socks.socksocket()
sock.set_proxy(socks.SOCKS5, "localhost", 1080)

# FIXME: Should be set with the server ip
# You can find using `docker inspect server | grep IPAddress`
# Bind to target
sock.connect(('172.18.0.3', 8080))

# Construct packet
ether=Ether()
ip=IP(dst='127.0.0.1')
tcp=TCP(dport=8080)

packet=ether/ip/tcp

sock.send(bytes(packet))
data=sock.recv(1024)
print(data)
