import argparse

from colorama import init

from core.session import CaptureSession

init(autoreset=True)


class Application:

    def __init__(self):

        self.session = CaptureSession()

    def build_parser(self):

        parser = argparse.ArgumentParser(
            prog="PySniffer",
            description="Python Network Packet Analyzer",
        )

        parser.add_argument(
            "--interface",
            help="Network interface"
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
            help="Packet count"
        )

        parser.add_argument(
            "--json",
            help="Export JSON"
        )

        parser.add_argument(
            "--csv",
            help="Export CSV"
        )

        return parser

    def run(self):

        parser = self.build_parser()

        args = parser.parse_args()

        self.session.start(args)