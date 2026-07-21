from scanner.capture import capture_packets
from scanner.parser import parse_packet
from scanner.statistics import Statistics
from scanner.exporter import Exporter
from scanner.filters import validate_filter, get_bpf_filter


class CaptureSession:

    def __init__(self):

        self.statistics = Statistics()
        self.exporter = Exporter()

        self.args = None

    def handle_packet(self, packet):

        parsed = parse_packet(packet)

        self.statistics.update(parsed)

        self.exporter.add_packet(parsed)

        print(
            f"{parsed['time']} "
            f"{parsed['source']} -> "
            f"{parsed['destination']} "
            f"[{parsed['protocol']}] "
            f"{parsed['size']} bytes"
        )

    def start(self, args):

        self.args = args

        protocol_filter = None

        if args.protocol_filter:

            protocol_filter = validate_filter(
                args.protocol_filter
            )

            if protocol_filter is None:

                raise ValueError(
                    "Invalid protocol filter."
                )

        bpf_filter = get_bpf_filter(protocol_filter)

        capture_packets(
            interface=args.interface,
            count=args.count,
            packet_filter=bpf_filter,
            callback=self.handle_packet,
        )

        print()

        self.statistics.report()

        if args.json:

            self.exporter.export_json(args.json)

        if args.csv:

            self.exporter.export_csv(args.csv)