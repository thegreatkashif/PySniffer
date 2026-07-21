from rich.panel import Panel
from rich.table import Table


def header(
    interface="Automatic",
    status="Capturing",
    packets=0,
    traffic="0 B",
):
    table = Table.grid(expand=True)

    table.add_column(justify="left")
    table.add_column(justify="left")
    table.add_column(justify="left")
    table.add_column(justify="left")

    table.add_row(
        f"[cyan]Interface:[/cyan] {interface}",
        f"[green]Status:[/green] {status}",
        f"[yellow]Packets:[/yellow] {packets}",
        f"[magenta]Traffic:[/magenta] {traffic}",
    )

    return Panel(
        table,
        title="[bold cyan]PySniffer v1.0[/bold cyan]",
        border_style="cyan",
    )