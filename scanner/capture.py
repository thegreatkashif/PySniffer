from scapy.all import sniff, rdpcap


def capture_packets(
    callback,
    interface=None,
    count=0,
    packet_filter=None,
):

    sniff(
        iface=interface,
        prn=callback,
        filter=packet_filter if packet_filter else None,
        count=count,
        store=False,
    )


def read_pcap(filename, callback):

    packets = rdpcap(filename)

    for packet in packets:

        callback(packet)