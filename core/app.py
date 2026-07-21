import argparse
import sys

from core.session import CaptureSession
from scanner.interfaces import list_interfaces


class Application:

    def __init__(self):

        self.session = CaptureSession()

    def build_parser(self):

        parser = argparse.ArgumentParser(
            prog="PySniffer",
            description="Python Packet Analyzer"
        )

        parser.add_argument(
            "--interface",
            help="Capture interface"
        )

        parser.add_argument(
            "--filter",
            dest="protocol_filter",
            help="Protocol filter"
        )

        parser.add_argument(
            "--count",
            type=int,
            default=0,
            help="Number of packets"
        )

        parser.add_argument(
            "--json",
            help="Export JSON"
        )

        parser.add_argument(
            "--csv",
            help="Export CSV"
        )
        
        parser.add_argument(
            "--pcap",
            help="Export packets to PCAP"
        )

        parser.add_argument(
            "--list-interfaces",
            action="store_true",
            help="List available interfaces"
        )

        return parser

    def run(self):

        parser = self.build_parser()

        args = parser.parse_args()

        if args.list_interfaces:

            print()
            print("=" * 80)
            print("AVAILABLE NETWORK INTERFACES")
            print("=" * 80)

            interfaces = list_interfaces()

            for index, iface in enumerate(interfaces, start=1):

                print(f"[{index}] {iface['name']}")

                if iface["description"]:
                    print(f"     {iface['description']}")

                print()

            sys.exit(0)

        self.session.run(args)