from scapy.all import *
from encryptor import encryptor
from decryptor import decryptor

print(encryptor("Hello World!"))

input_iface = "veth0"
input_iface_ip = "192.168.100.1"
stimuli_iface = "veth1"
stimuli_iface_ip = "192.168.100.2"
outgoing_iface = "PLACEHOLDER"

# Check if incoming packet is relevent, valid and should be processed
# For example: if packet's 3rd layer protocol == IP
def check_pkt(pkt):
    return True

# Extract payload from packet to encrypt as bytes/string. May include higher-layer headers.
def get_payload_to_encrypt(pkt):
    return "placeholder"

# Reconstruct packet with new encrypted payload to send out
# With updated addresses
def reconstruct_encrypted_pkt(encrypted_payload):
    return Ether()/IP()/Raw(load=encrypted_payload) # Placeholder!

# Example template for *one-way* encryptor
def process_packet_one_way(pkt):
    if not check_pkt(pkt):
        return
    
    payload_to_encrypt = get_payload_to_encrypt(pkt)

    encrypted_payload = encryptor(payload_to_encrypt)

    outgoing_encrypted_pkt = reconstruct_encrypted_pkt(encrypted_payload)

    #sendp(outgoing_encrypted_pkt, iface=outgoing_iface)

    # if pkt.haslayer(IP):
    #     pkt_src_ip = pkt[IP].src
    #     pkt_dst_ip = pkt[IP].dst
    #     if pkt_src_ip == stimuli_iface_ip and pkt_dst_ip == input_iface_ip:
    #         print(f"Received: {pkt.summary()}")
    #         pkt[IP].show()
    #         print(f"Raw payload: {pkt[Raw].load}")

sniff(iface=input_iface, prn=process_packet_one_way)