import socket
from datetime import datetime

from scapy.all import IP, IPv6, TCP, UDP


HOST_CACHE = {}


def resolve_host(ip):

    if ip in HOST_CACHE:
        return HOST_CACHE[ip]

    try:

        hostname = socket.gethostbyaddr(ip)[0]

    except Exception:

        hostname = ip

    HOST_CACHE[ip] = hostname

    return hostname


def protocol_name(packet):

    if packet.haslayer(TCP):

        sport = packet[TCP].sport
        dport = packet[TCP].dport

        ports = {80: "HTTP", 443: "HTTPS", 22: "SSH", 21: "FTP", 25: "SMTP", 53: "DNS"}

        if sport in ports:
            return ports[sport]

        if dport in ports:
            return ports[dport]

        return "TCP"

    if packet.haslayer(UDP):

        sport = packet[UDP].sport
        dport = packet[UDP].dport

        if sport == 53 or dport == 53:
            return "DNS"

        if sport == 67 or dport == 67:
            return "DHCP"

        return "UDP"

    return packet.lastlayer().name


def parse_packet(packet):

    source = "-"
    destination = "-"

    if packet.haslayer(IP):

        source = packet[IP].src
        destination = packet[IP].dst

    elif packet.haslayer(IPv6):

        source = packet[IPv6].src
        destination = packet[IPv6].dst

    source_port = "-"
    destination_port = "-"

    if packet.haslayer(TCP):

        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif packet.haslayer(UDP):

        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    return {

        "time": datetime.now().strftime("%H:%M:%S"),

        "source": source,
        "destination": destination,

        "source_host": resolve_host(source),
        "destination_host": resolve_host(destination),

        "protocol": protocol_name(packet),

        "source_port": source_port,
        "destination_port": destination_port,

        "size": len(packet),
    }