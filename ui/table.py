from rich.table import Table


def packet_table():

    table = Table()

    table.add_column("Time", style="cyan")

    table.add_column("Source")

    table.add_column("Destination")

    table.add_column("Protocol")

    table.add_column("Sport")

    table.add_column("Dport")

    table.add_column("Size")

    return table