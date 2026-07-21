import argparse

from colorama import Fore, init

from scanner.capture import capture_packets
from scanner.parser import parse_packet
from scanner.display import print_header, display_packet


init(autoreset=True)


def banner():
    print(Fore.CYAN + "=" * 70)
    print(Fore.GREEN + "PySniffer - Python Packet Analyzer")
    print(Fore.CYAN + "=" * 70)


def handle_packet(packet):
    """
    Parse and display each captured packet.
    """

    packet_data = parse_packet(packet)

    display_packet(packet_data)


def main():
    parser = argparse.ArgumentParser(
        prog="PySniffer",
        description="A Python-based network packet analyzer."
    )

    parser.add_argument(
        "--interface",
        help="Network interface used for packet capture"
    )

    parser.add_argument(
        "--filter",
        help="Capture filter such as tcp, udp, or icmp"
    )

    parser.add_argument(
        "--count",
        type=int,
        default=0,
        help="Number of packets to capture (0 = unlimited)"
    )

    parser.add_argument(
        "--json",
        help="Export captured packets to JSON"
    )

    parser.add_argument(
        "--csv",
        help="Export captured packets to CSV"
    )

    args = parser.parse_args()

    banner()

    print(f"Interface : {args.interface or 'Automatic'}")
    print(f"Filter    : {args.filter or 'None'}")
    print(f"Count     : {args.count or 'Unlimited'}")

    print(
        Fore.YELLOW
        + "\nStarting packet capture..."
    )

    print(
        Fore.YELLOW
        + "Press Ctrl+C to stop an unlimited capture.\n"
    )

    print_header()

    try:
        capture_packets(
            interface=args.interface,
            count=args.count,
            packet_filter=args.filter,
            callback=handle_packet,
        )

    except PermissionError:
        print(
            Fore.RED
            + "\nPermission denied. Run PowerShell as Administrator."
        )

    except KeyboardInterrupt:
        print(
            Fore.YELLOW
            + "\nCapture stopped by user."
        )

    except Exception as error:
        print(
            Fore.RED
            + f"\nCapture error: {error}"
        )

    print(
        Fore.CYAN
        + "\nCapture complete."
    )


if __name__ == "__main__":
    main()