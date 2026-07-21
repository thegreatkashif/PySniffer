from collections import Counter


class Statistics:

    def __init__(self):
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

    def report(self):

        print()

        print("=" * 60)

        print("CAPTURE STATISTICS")

        print("=" * 60)

        print(f"Packets Captured : {self.total_packets}")

        print(f"Total Bytes      : {self.total_bytes}")

        if self.total_packets:

            avg = self.total_bytes // self.total_packets

        else:

            avg = 0

        print(f"Average Size     : {avg} bytes")

        print()

        print("Protocol Counts")

        print("-" * 40)

        for protocol, count in self.protocols.items():

            print(f"{protocol:<15}{count}")

        print()

        print("Top Source Hosts")

        print("-" * 40)

        for host, count in self.sources.most_common(5):

            print(f"{host:<25}{count}")

        print()

        print("Top Destination Hosts")

        print("-" * 40)

        for host, count in self.destinations.most_common(5):

            print(f"{host:<25}{count}")