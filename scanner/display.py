from colorama import Fore, Style


def print_header():
    """
    Print the packet table header.
    """

    print(
        f"{'TIME':<10}"
        f"{'SOURCE':<26}"
        f"{'DESTINATION':<26}"
        f"{'PROTOCOL':<11}"
        f"{'SPORT':<9}"
        f"{'DPORT':<9}"
        f"{'SIZE':<8}"
    )

    print("-" * 99)


def protocol_color(protocol):
    """
    Return a terminal color for each protocol.
    """

    colors = {
        "TCP": Fore.GREEN,
        "UDP": Fore.BLUE,
        "DNS": Fore.CYAN,
        "HTTP": Fore.YELLOW,
        "HTTPS": Fore.MAGENTA,
        "ICMP": Fore.RED,
        "ICMPv6": Fore.RED,
        "ARP": Fore.YELLOW,
        "DHCP": Fore.CYAN,
        "IPv4": Fore.WHITE,
        "IPv6": Fore.WHITE,
    }

    return colors.get(protocol, Fore.WHITE)


def display_packet(packet_data):
    """
    Display a parsed packet as a formatted table row.
    """

    protocol = packet_data["protocol"]

    color = protocol_color(protocol)

    print(
        f"{packet_data['time']:<10}"
        f"{packet_data['source']:<26}"
        f"{packet_data['destination']:<26}"
        f"{color}{protocol:<11}{Style.RESET_ALL}"
        f"{str(packet_data['source_port']):<9}"
        f"{str(packet_data['destination_port']):<9}"
        f"{packet_data['size']:<8}"
    )