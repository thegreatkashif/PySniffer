import threading

from scanner.capture import capture_packets
from scanner.exporter import Exporter
from scanner.filters import get_bpf_filter, validate_filter
from scanner.parser import parse_packet
from scanner.statistics import Statistics
from ui.dashboard import Dashboard


class CaptureSession:

    def __init__(self):

        self.dashboard = Dashboard()
        self.statistics = Statistics()
        self.exporter = Exporter()

        self.args = None

    def handle_packet(self, packet):

        parsed = parse_packet(packet)

        self.statistics.update(parsed)

        self.exporter.add_packet(
            parsed,
            packet
        )

        self.dashboard.update(
            parsed,
            self.statistics.snapshot()
        )

    def capture_worker(self):

        protocol_filter = None

        if self.args.protocol_filter:

            protocol_filter = validate_filter(
                self.args.protocol_filter
            )

            if protocol_filter is None:
                raise ValueError("Invalid protocol filter")

        capture_packets(
            interface=self.args.interface,
            count=self.args.count,
            packet_filter=get_bpf_filter(protocol_filter),
            callback=self.handle_packet,
        )

    def run(self, args):

        self.args = args

        worker = threading.Thread(
            target=self.capture_worker,
            daemon=True,
        )

        with self.dashboard.start() as live:

            worker.start()

            while worker.is_alive():

                self.dashboard.refresh()

                live.update(self.dashboard.layout)

                worker.join(timeout=0.05)

            self.dashboard.refresh()

            live.update(self.dashboard.layout)

        print()

        self.statistics.report()

        if args.json:
            self.exporter.export_json(args.json)

        if args.csv:
            self.exporter.export_csv(args.csv)

        if getattr(args, "pcap", None):
            self.exporter.export_pcap(args.pcap)