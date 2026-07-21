from collections import Counter
import time


class Statistics:

    def __init__(self):

        self.start_time = time.time()

        self.total_packets = 0
        self.total_bytes = 0

        self.protocols = Counter()
        self.sources = Counter()
        self.destinations = Counter()

    def update(self, packet):

        self.total_packets += 1
        self.total_bytes += packet["size"]

        self.protocols[packet["protocol"]] += 1
        self.sources[packet["source"]] += 1
        self.destinations[packet["destination"]] += 1

    def duration(self):

        return time.time() - self.start_time

    def packets_per_second(self):

        d = self.duration()

        if d <= 0:
            return 0

        return self.total_packets / d

    def bytes_per_second(self):

        d = self.duration()

        if d <= 0:
            return 0

        return self.total_bytes / d

    def human_size(self, size):

        units = ["B", "KB", "MB", "GB"]

        index = 0

        while size >= 1024 and index < len(units) - 1:
            size /= 1024
            index += 1

        return f"{size:.2f} {units[index]}"

    def snapshot(self):

        return {
            "packets": self.total_packets,
            "bytes": self.total_bytes,
            "duration": self.duration(),
            "pps": self.packets_per_second(),
            "bps": self.bytes_per_second(),
            "protocols": dict(self.protocols),
            "sources": dict(self.sources),
            "destinations": dict(self.destinations),
        }

    def report(self):

        print()

        print("=" * 65)
        print("CAPTURE SUMMARY")
        print("=" * 65)

        print(f"Duration           : {self.duration():.2f} seconds")
        print(f"Packets Captured   : {self.total_packets}")
        print(f"Total Data         : {self.human_size(self.total_bytes)}")

        average = 0

        if self.total_packets:
            average = self.total_bytes / self.total_packets

        print(f"Average Packet     : {average:.2f} bytes")
        print(f"Packets / Second   : {self.packets_per_second():.2f}")
        print(f"Bytes / Second     : {self.human_size(self.bytes_per_second())}")

        print()

        print("Protocol Distribution")
        print("-" * 40)

        for protocol, count in self.protocols.most_common():
            print(f"{protocol:<20}{count}")

        print()

        print("Top Source Hosts")
        print("-" * 40)

        for host, count in self.sources.most_common(5):
            print(f"{host:<30}{count}")

        print()

        print("Top Destination Hosts")
        print("-" * 40)

        for host, count in self.destinations.most_common(5):
            print(f"{host:<30}{count}")