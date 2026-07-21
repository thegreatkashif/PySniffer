import csv
import json


class Exporter:

    def __init__(self):
        self.packets = []

    def add_packet(self, packet):

        self.packets.append(packet)

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