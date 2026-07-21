import socket
from datetime import datetime

from scapy.all import (
    ARP,
    DNS,
    ICMP,
    IP,
    IPv6,
    TCP,
    UDP,
)


HOST_CACHE = {}


def resolve_host(ip):

    if ip in HOST_CACHE:
        return HOST_CACHE[ip]

    try:
        HOST_CACHE[ip] = socket.gethostbyaddr(ip)[0]
    except Exception:
        HOST_CACHE[ip] = ip

    return HOST_CACHE[ip]


def protocol_name(packet):

    if packet.haslayer(ARP):
        return "ARP"

    if packet.haslayer(DNS):
        return "DNS"

    if packet.haslayer(ICMP):
        return "ICMP"

    if packet.haslayer(TCP):

        sport = packet[TCP].sport
        dport = packet[TCP].dport

        ports = {
            20: "FTP",
            21: "FTP",
            22: "SSH",
            23: "TELNET",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS",
            465: "SMTPS",
            587: "SMTP",
            993: "IMAPS",
            995: "POP3S",
            3306: "MySQL",
            3389: "RDP",
            5432: "PostgreSQL",
            6379: "Redis",
            8080: "HTTP-ALT",
            8443: "HTTPS-ALT",
        }

        if sport in ports:
            return ports[sport]

        if dport in ports:
            return ports[dport]

        return "TCP"

    if packet.haslayer(UDP):

        sport = packet[UDP].sport
        dport = packet[UDP].dport

        ports = {
            53: "DNS",
            67: "DHCP",
            68: "DHCP",
            69: "TFTP",
            123: "NTP",
            161: "SNMP",
            443: "QUIC",
            5353: "mDNS",
        }

        if sport in ports:
            return ports[sport]

        if dport in ports:
            return ports[dport]

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