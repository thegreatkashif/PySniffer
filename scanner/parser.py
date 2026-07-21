from datetime import datetime

from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.inet6 import IPv6, ICMPv6ND_RA
from scapy.layers.l2 import ARP


def get_protocol(packet):
    if packet.haslayer(ARP):
        return "ARP"

    if packet.haslayer(ICMPv6ND_RA):
        return "ICMPv6"

    if packet.haslayer(ICMP):
        return "ICMP"

    if packet.haslayer(TCP):
        tcp = packet[TCP]

        if tcp.sport == 80 or tcp.dport == 80:
            return "HTTP"

        if tcp.sport == 443 or tcp.dport == 443:
            return "HTTPS"

        return "TCP"

    if packet.haslayer(UDP):
        udp = packet[UDP]

        if udp.sport == 53 or udp.dport == 53:
            return "DNS"

        if udp.sport in (67, 68) or udp.dport in (67, 68):
            return "DHCP"

        return "UDP"

    if packet.haslayer(IPv6):
        return "IPv6"

    if packet.haslayer(IP):
        return "IPv4"

    return "OTHER"


def parse_packet(packet):
    timestamp = datetime.fromtimestamp(
        float(packet.time)
    ).strftime("%H:%M:%S")

    source = "-"
    destination = "-"
    source_port = "-"
    destination_port = "-"

    if packet.haslayer(IP):
        source = packet[IP].src
        destination = packet[IP].dst

    elif packet.haslayer(IPv6):
        source = packet[IPv6].src
        destination = packet[IPv6].dst

    elif packet.haslayer(ARP):
        source = packet[ARP].psrc
        destination = packet[ARP].pdst

    if packet.haslayer(TCP):
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif packet.haslayer(UDP):
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    return {
        "time": timestamp,
        "source": source,
        "destination": destination,
        "protocol": get_protocol(packet),
        "source_port": source_port,
        "destination_port": destination_port,
        "size": len(packet),
    }