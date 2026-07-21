import argparse
import sys

from core.session import CaptureSession
from scanner.filters import available_filters
from scanner.interfaces import list_interfaces


class Application:

    def __init__(self):

        self.session = CaptureSession()

    def build_parser(self):

        parser = argparse.ArgumentParser(
            prog="PySniffer",
            description="Professional Packet Analyzer",
        )

        parser.add_argument("--interface")
        parser.add_argument("--filter", dest="protocol_filter")
        parser.add_argument("--count", type=int, default=0)

        parser.add_argument("--json")
        parser.add_argument("--csv")
        parser.add_argument("--pcap")
        parser.add_argument("--pcap-read")

        parser.add_argument(
            "--list-interfaces",
            action="store_true"
        )

        parser.add_argument(
            "--list-filters",
            action="store_true"
        )

        return parser

    def run(self):

        parser = self.build_parser()

        args = parser.parse_args()

        if args.list_interfaces:

            print("\nAvailable Interfaces\n")

            for index, iface in enumerate(
                list_interfaces(),
                start=1
            ):

                print(f"{index}. {iface['name']}")

            sys.exit()

        if args.list_filters:

            print("\nAvailable Filters\n")

            for item in available_filters():

                print(item)

            sys.exit()

        self.session.run(args)