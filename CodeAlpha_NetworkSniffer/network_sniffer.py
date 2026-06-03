from scapy.all import *

def packet_callback(packet):
    print("\n=== Packet Captured ===")

    if packet.haslayer(IP):
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

        if packet.haslayer(TCP):
            print("Protocol: TCP")
        elif packet.haslayer(UDP):
            print("Protocol: UDP")
        elif packet.haslayer(ICMP):
            print("Protocol: ICMP")
        else:
            print("Protocol: Other")

print("Starting Network Sniffer...")

sniff(prn=packet_callback, count=10)

print("Sniffing Completed!")