import argparse

from colorama import Fore, init

from scanner.capture import capture_packets
from scanner.parser import parse_packet
from scanner.display import print_header, display_packet

from scanner.statistics import Statistics
from scanner.filters import (
    VALID_FILTERS,
    validate_filter,
    get_bpf_filter,
)


init(autoreset=True)
stats = Statistics()


def banner():
    print(Fore.CYAN + "=" * 70)
    print(Fore.GREEN + "PySniffer - Python Packet Analyzer")
    print(Fore.CYAN + "=" * 70)


def handle_packet(packet):

    packet_data = parse_packet(packet)

    stats.update(packet_data)

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
        dest="protocol_filter",
        help=(
            "Protocol filter: "
            + ", ".join(sorted(VALID_FILTERS))
        )
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

    if args.count < 0:
        parser.error("--count cannot be negative.")

    protocol_filter = None

    if args.protocol_filter:
        protocol_filter = validate_filter(
            args.protocol_filter
        )

        if protocol_filter is None:
            parser.error(
                "Invalid filter. Available filters: "
                + ", ".join(sorted(VALID_FILTERS))
            )

    bpf_filter = get_bpf_filter(protocol_filter)

    banner()

    print(
        f"Interface : "
        f"{args.interface or 'Automatic'}"
    )

    print(
        f"Filter    : "
        f"{protocol_filter or 'None'}"
    )

    print(
        f"Count     : "
        f"{args.count or 'Unlimited'}"
    )

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
            packet_filter=bpf_filter,
            callback=handle_packet,
        )

    except PermissionError:
        print(
            Fore.RED
            + "\nPermission denied. "
            + "Run PowerShell as Administrator."
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

    stats.report()


if __name__ == "__main__":
    main()