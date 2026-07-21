from collections import deque

from rich.console import Console
from rich.layout import Layout
from rich.live import Live

from ui.header import header
from ui.footer import footer
from ui.table import packet_table


console = Console()


class Dashboard:

    MAX_ROWS = 100

    def __init__(self):

        self.rows = deque(maxlen=self.MAX_ROWS)

        self.packet_count = 0
        self.total_bytes = 0

        self.layout = Layout()

        self.layout.split_column(
            Layout(name="header", size=5),
            Layout(name="table"),
            Layout(name="footer", size=3),
        )

        self.table = packet_table()

        self.refresh()

    def human_size(self, size):

        units = ["B", "KB", "MB", "GB"]

        i = 0

        while size >= 1024 and i < len(units) - 1:
            size /= 1024
            i += 1

        return f"{size:.2f} {units[i]}"

    def add_packet(self, packet):

        self.packet_count += 1

        self.total_bytes += packet["size"]

        self.rows.append(packet)

    def refresh(self):

        table = packet_table()

        for packet in self.rows:

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
                packets=self.packet_count,
                traffic=self.human_size(self.total_bytes),
            )
        )

        self.layout["table"].update(table)

        self.layout["footer"].update(footer())

    def start(self):

        return Live(
            self.layout,
            refresh_per_second=30,
            console=console,
            screen=True,
        )