from rich.panel import Panel
from rich.table import Table


def build_stats(stats):

    table = Table(expand=True)

    table.add_column("Metric", style="cyan")
    table.add_column("Value", justify="right")

    table.add_row("Packets", str(stats.get("packets", 0)))
    table.add_row("Traffic", stats.get("traffic", "0 B"))
    table.add_row("Duration", f"{stats.get('duration', 0):.1f}s")
    table.add_row("Packets/sec", f"{stats.get('pps', 0):.2f}")
    table.add_row("Bytes/sec", stats.get("bps_human", "0 B"))

    table.add_section()

    table.add_row("[bold green]Protocols[/bold green]", "")

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

            if len(host) > 25:
                host = host[:22] + "..."

            table.add_row(host, str(count))
    else:
        table.add_row("-", "-")

    table.add_section()

    table.add_row("[bold magenta]Top Destinations[/bold magenta]", "")

    destinations = stats.get("destinations", {})

    if destinations:
        for host, count in sorted(
            destinations.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]:

            if len(host) > 25:
                host = host[:22] + "..."

            table.add_row(host, str(count))
    else:
        table.add_row("-", "-")

    return Panel(
        table,
        title="[bold green]Live Statistics[/bold green]",
        border_style="green",
    )