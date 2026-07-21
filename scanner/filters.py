VALID_FILTERS = {
    "arp": "arp",
    "dns": "port 53",
    "http": "port 80",
    "https": "port 443",
    "tcp": "tcp",
    "udp": "udp",
    "icmp": "icmp",
    "dhcp": "port 67 or port 68",
    "ssh": "port 22",
    "ftp": "port 20 or port 21",
    "smtp": "port 25",
    "pop3": "port 110",
    "imap": "port 143",
    "rdp": "port 3389",
    "mysql": "port 3306",
    "postgres": "port 5432",
    "redis": "port 6379",
    "ntp": "port 123",
    "snmp": "port 161",
    "mdns": "port 5353",
    "quic": "udp port 443",
}


def validate_filter(filter_name):

    if filter_name is None:
        return None

    filter_name = filter_name.lower()

    if filter_name not in VALID_FILTERS:

        raise ValueError(
            "Invalid filter. Available filters: "
            + ", ".join(sorted(VALID_FILTERS.keys()))
        )

    return filter_name


def get_bpf_filter(filter_name):

    if filter_name is None:
        return None

    return VALID_FILTERS[filter_name]


def available_filters():

    return sorted(VALID_FILTERS.keys())