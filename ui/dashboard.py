from collections import deque

from rich.console import Console
from rich.live import Live
from rich.layout import Layout

from ui.header import header
from ui.footer import footer
from ui.table import packet_table


console = Console()


class Dashboard:

    MAX_ROWS = 100

    def __init__(self):

        self.layout = Layout()

        self.layout.split_column(
            Layout(name="header", size=5),
            Layout(name="table"),
            Layout(name="footer", size=5),
        )

        self.rows = deque(maxlen=self.MAX_ROWS)

        self.table = packet_table()

        self.layout["header"].update(header())
        self.layout["table"].update(self.table)
        self.layout["footer"].update(footer())

    def add_packet(self, packet):

        self.rows.append(packet)

        self.refresh()

    def refresh(self):

        self.table = packet_table()

        for packet in self.rows:

            self.table.add_row(
                packet["time"],
                packet["source"],
                packet["destination"],
                packet["protocol"],
                str(packet["source_port"]),
                str(packet["destination_port"]),
                str(packet["size"]),
            )

        self.layout["table"].update(self.table)

    def start(self):

        return Live(
            self.layout,
            console=console,
            refresh_per_second=30,
            screen=True,
        )