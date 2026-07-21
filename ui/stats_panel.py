from rich.panel import Panel
from rich.table import Table


def build_stats(stats):

    table = Table(
        show_header=True,
        header_style="bold cyan",
        expand=True
    )

    table.add_column("Metric")
    table.add_column("Value", justify="right")

    table.add_row("Packets", str(stats.get("packets", 0)))
    table.add_row("Traffic", stats.get("traffic", "0 B"))
    table.add_row("Duration", f"{stats.get('duration', 0):.1f}s")
    table.add_row("Packets/sec", f"{stats.get('pps', 0):.2f}")
    table.add_row("Bytes/sec", stats.get("bps_human", "0 B"))

    table.add_section()

    table.add_row("[bold green]Top Protocols[/bold green]", "")

    protocols = stats.get("protocols", {})

    if protocols:

        for protocol, count in sorted(
            protocols.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]:

            table.add_row(protocol, str(count))

    else:

        table.add_row("-", "-")

    table.add_section()

    table.add_row("[bold yellow]Top Sources[/bold yellow]", "")

    sources = stats.get("sources", {})

    if sources:

        for host, count in sorted(
            sources.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]:

            table.add_row(host, str(count))

    else:

        table.add_row("-", "-")

    return Panel(
        table,
        title="[bold]Live Statistics[/bold]",
        border_style="green"
    )