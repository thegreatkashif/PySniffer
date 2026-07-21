from collections import deque
from threading import Lock

from rich.console import Console
from rich.layout import Layout
from rich.live import Live

from ui.footer import footer
from ui.header import header
from ui.table import packet_table
from ui.stats_panel import build_stats


console = Console()


class Dashboard:

    MAX_ROWS = 100

    def __init__(self):

        self.rows = deque(maxlen=self.MAX_ROWS)

        self.lock = Lock()

        self.stats = {
            "packets": 0,
            "bytes": 0,
            "traffic": "0 B",
            "duration": 0,
            "pps": 0,
            "bps": 0,
            "bps_human": "0 B",
            "protocols": {},
            "sources": {},
            "destinations": {},
        }

        self.layout = Layout()

        self.layout.split_column(
            Layout(name="header", size=7),
            Layout(name="body"),
            Layout(name="footer", size=3),
        )

        self.layout["body"].split_row(
            Layout(name="packets", ratio=3),
            Layout(name="stats", ratio=1),
        )

        self.refresh()

    def human_size(self, size):

        units = ["B", "KB", "MB", "GB"]

        index = 0

        while size >= 1024 and index < len(units) - 1:
            size /= 1024
            index += 1

        return f"{size:.2f} {units[index]}"

    def update(self, packet, stats):

        with self.lock:

            self.rows.append(packet)

            stats = dict(stats)

            stats["traffic"] = self.human_size(
                stats.get("bytes", 0)
            )

            stats["bps_human"] = self.human_size(
                stats.get("bps", 0)
            )

            self.stats = stats

    def refresh(self):

        with self.lock:

            packets = list(self.rows)

            stats = dict(self.stats)

        table = packet_table()

        for packet in packets:

            table.add_row(
                packet["time"],
                packet["source"],
                packet["destination"],
                packet["protocol"],
                str(packet["source_port"]),
                str(packet["destination_port"]),
                str(packet["size"]),
            )

        self.layout["header"].update(
            header(
                interface="Automatic",
                status="Capturing",
                packets=stats.get("packets", 0),
                traffic=stats.get("traffic", "0 B"),
                duration=stats.get("duration", 0),
                pps=stats.get("pps", 0),
            )
        )

        self.layout["packets"].update(table)

        self.layout["stats"].update(
            build_stats(stats)
        )

        self.layout["footer"].update(
            footer()
        )

    def start(self):

        return Live(
            self.layout,
            console=console,
            refresh_per_second=30,
            screen=True,
        )