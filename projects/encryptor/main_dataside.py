from scapy.all import *
from encryptor import encryptor
from decryptor import decryptor

VALID_PKT_FROM_RED = 0
VALID_PKT_FROM_BLACK = 1
INVALID_PKT = -1

main_iface = "ENTER INTERFACE NAME HERE"
main_iface_ip = "ENTER IP HERE"
red_machine_ip = "ENTER IP HERE"
black_machine_ip = "ENTER IP HERE"

# Check if incoming packet is valid and if it's coming from red or black network
# For example: check existance of IP header, if source IP is known...
def check_pkt(pkt):
    return INVALID_PKT

# Extract payload from packet to encrypt as bytes/string. May include higher-layer headers.
def get_payload_to_encrypt(pkt):
    return "Hi! I'm a placeholder payload :)"

# Extract encrypted payload from packet to decrypt as bytes/string. 
# Note: Logic depends on which headers were encrypted too
def get_payload_to_decrypt(pkt):
    return "Hi! I'm a placeholder payload :)"

# Reconstruct packet with new encrypted payload bytes to send out
# With updated addresses
def reconstruct_encrypted_pkt(encrypted_payload):
    return "Replace me with a packet!"

# Reconstruct packet with decrypted payload bytes to send out
# With updated addresses
def reconstruct_decrypted_pkt(decrypted_payload):
    return "Replace me with a packet!"

# Example of two-way packet handling
def process_packet(pkt):
    pkt_status = check_pkt(pkt)

    # If packet is invalid/irrelevant, ignore it
    if pkt_status == INVALID_PKT:
        return
    # If packet from red network/machine, we need to encrypt it and send to black network/machine
    elif pkt_status == VALID_PKT_FROM_RED:
        payload_to_encrypt = get_payload_to_encrypt(pkt) # Extract portion we want to encrypt
        encrypted_payload = encryptor(payload_to_encrypt) # Encrypt it
        outgoing_pkt = reconstruct_encrypted_pkt(encrypted_payload) # Build new packet with encrypted payload
    # Otherwise, it came from black network/computer and we need to decrypt it and send to red
    else: 
        payload_to_decrypt = get_payload_to_decrypt(pkt) # Get encrypted portion of packet
        decrypted_payload = decryptor(payload_to_decrypt) # Decrypt it
        outgoing_pkt = reconstruct_decrypted_pkt(decrypted_payload) # Construct full valid decrypted packet to send
    
    # Send new packet through interface
    sendp(outgoing_pkt, iface=main_iface)

# Monitor interface for traffic and handle each packet
sniff(iface=main_iface, prn=process_packet)