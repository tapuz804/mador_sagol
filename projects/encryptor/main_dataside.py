from scapy.all import *
from encryptor import encryptor
from decryptor import decryptor

input_iface = "ENTER INTERFACE NAME HERE"
input_iface_ip = "ENTER IP HERE"
outgoing_iface = "ENTER INTERFACE NAME HERE"

# Check if incoming packet is relevent, valid and should be processed
# For example: if packet's 3rd layer protocol == IP, or if source IP is known
def check_pkt(pkt):
    return True

# Extract payload from packet to encrypt as bytes/string. May include higher-layer headers.
def get_payload_to_encrypt(pkt):
    return "Hi! I'm a placeholder payload :)"

# Reconstruct packet with new encrypted payload to send out
# With updated addresses
def reconstruct_encrypted_pkt(encrypted_payload):
    return "Replace me with a packet!"

# Example template for *one-way* encryptor
def process_packet_one_way(pkt):
    if not check_pkt(pkt):
        return
    
    payload_to_encrypt = get_payload_to_encrypt(pkt)

    encrypted_payload = encryptor(payload_to_encrypt)

    outgoing_encrypted_pkt = reconstruct_encrypted_pkt(encrypted_payload)

    sendp(outgoing_encrypted_pkt, iface=outgoing_iface)

# Monitor interface for traffic and handle each packet
sniff(iface=input_iface, prn=process_packet_one_way)