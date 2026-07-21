from scapy.all import sniff


def capture_packets(interface=None, count=0, packet_filter=None, callback=None):
    """
    Capture network packets using Scapy.

    interface:
        Network interface name. None lets Scapy choose the default.

    count:
        Number of packets to capture.
        0 means capture continuously until Ctrl+C.

    packet_filter:
        BPF capture filter such as "tcp", "udp", or "icmp".

    callback:
        Function called whenever a packet is captured.
    """

    sniff(
        iface=interface,
        count=count,
        filter=packet_filter,
        prn=callback,
        store=False,
    )