VALID_FILTERS = {
    "tcp",
    "udp",
    "icmp",
    "arp",
    "dns",
    "http",
    "https",
    "dhcp",
}


def validate_filter(protocol_filter):
    """
    Validate a user-provided protocol filter.
    """

    if protocol_filter is None:
        return None

    protocol_filter = protocol_filter.lower().strip()

    if protocol_filter not in VALID_FILTERS:
        return None

    return protocol_filter


def get_bpf_filter(protocol_filter):
    """
    Convert a PySniffer protocol filter into a BPF capture filter.
    """

    filters = {
        "tcp": "tcp",
        "udp": "udp",
        "icmp": "icmp",
        "arp": "arp",
        "dns": "port 53",
        "http": "tcp port 80",
        "https": "tcp port 443",
        "dhcp": "udp and (port 67 or port 68)",
    }

    return filters.get(protocol_filter)