from rich.panel import Panel
from rich.table import Table


def format_duration(seconds):

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    return f"{hours:02}:{minutes:02}:{secs:02}"


def header(
    interface="Automatic",
    status="Capturing",
    packets=0,
    traffic="0 B",
    duration=0,
    pps=0,
):

    table = Table.grid(expand=True)

    table.add_column(justify="left")
    table.add_column(justify="left")
    table.add_column(justify="left")

    table.add_column(justify="left")
    table.add_column(justify="left")
    table.add_column(justify="left")

    table.add_row(
        f"[cyan]Interface[/cyan]\n{interface}",
        f"[green]Status[/green]\n{status}",
        f"[yellow]Duration[/yellow]\n{format_duration(duration)}",
        f"[magenta]Packets[/magenta]\n{packets}",
        f"[bright_blue]Traffic[/bright_blue]\n{traffic}",
        f"[red]PPS[/red]\n{pps:.2f}",
    )

    return Panel(
        table,
        title="[bold cyan]PySniffer v1.0[/bold cyan]",
        border_style="cyan",
    )