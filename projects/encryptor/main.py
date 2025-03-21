from scapy.all import *
import os
from encryptor import encryptor
from decryptor import decryptor

print(encryptor("Hello World!"))

input_iface = "tun0"
output_iface = "tun1"

def process_packet(pkt):
    print(f"Received: {pkt.summary()}")
    if IP in pkt:
        print(f"Received: {pkt.summary()}")

        # # Strip Layer 3 headers
        # payload = bytes(pkt[IP].payload)

        # # Encrypt the payload (dummy encryption here)
        # encrypted_payload = payload[::-1]  # Simple reverse for testing

        # # Reconstruct the packet with new headers
        # new_pkt = IP(dst="10.0.1.2") / encrypted_payload

        # # Send via output interface
        # send(new_pkt, iface=output_iface)
        # print(f"Forwarded: {new_pkt.summary()}")

# Sniff incoming packets on tun0
sniff(iface="lo", prn=process_packet)