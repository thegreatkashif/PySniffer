import csv
import json

from scapy.all import wrpcap


class Exporter:

    def __init__(self):

        self.packets = []
        self.raw_packets = []

    def add_packet(self, packet, raw_packet=None):

        self.packets.append(packet)

        if raw_packet is not None:
            self.raw_packets.append(raw_packet)

    def export_json(self, filename):

        with open(filename, "w", encoding="utf-8") as file:

            json.dump(
                self.packets,
                file,
                indent=4
            )

        print(f"\nJSON exported to {filename}")

    def export_csv(self, filename):

        if not self.packets:
            return

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=self.packets[0].keys()
            )

            writer.writeheader()

            writer.writerows(self.packets)

        print(f"\nCSV exported to {filename}")

    def export_pcap(self, filename):

        if not self.raw_packets:

            print("\nNo packets available to export.")

            return

        wrpcap(filename, self.raw_packets)

        print(f"\nPCAP exported to {filename}")