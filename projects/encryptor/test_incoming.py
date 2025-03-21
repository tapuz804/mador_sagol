from scapy.all import *
import os
from encryptor import encryptor
from decryptor import decryptor

print(encryptor("Hello World!"))

input_iface = "veth0"
input_iface_ip = "192.168.100.1"
input_iface_mac = "d2:64:ee:7e:98:5b"
stimuli_iface = "veth1"
stimuli_iface_ip = "192.168.100.2"
stimuli_iface_mac = "8e:29:d9:c5:a1:f7"

# Craft a simple ICMP Echo Request packet (ping)
packet = Ether(dst=input_iface_mac, src=stimuli_iface_mac)/IP(src=stimuli_iface_ip, dst=input_iface_ip)/Raw(load="Hello!")

# Send the packet
sendp(packet, iface=stimuli_iface)