import argparse
from colorama import Fore, Style, init

init(autoreset=True)


def banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.GREEN + "PySniffer - Python Packet Analyzer")
    print(Fore.CYAN + "=" * 50)


def main():
    parser = argparse.ArgumentParser(
        description="PySniffer - Network Packet Analyzer"
    )

    parser.add_argument(
        "--interface",
        help="Network interface to capture packets from"
    )

    parser.add_argument(
        "--filter",
        help="Protocol filter (tcp, udp, icmp, dns)"
    )

    parser.add_argument(
        "--json",
        help="Export captured packets to JSON"
    )

    parser.add_argument(
        "--csv",
        help="Export captured packets to CSV"
    )

    parser.add_argument(
        "--count",
        type=int,
        default=0,
        help="Number of packets to capture (0 = unlimited)"
    )

    args = parser.parse_args()

    banner()

    print(Fore.YELLOW + "Selected Options")
    print("-" * 50)
    print(f"Interface : {args.interface}")
    print(f"Filter    : {args.filter}")
    print(f"JSON File : {args.json}")
    print(f"CSV File  : {args.csv}")
    print(f"Count     : {args.count}")
    print("-" * 50)


if __name__ == "__main__":
    main()