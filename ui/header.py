from rich.panel import Panel


def header():

    return Panel.fit(
        "[bold cyan]PySniffer v1.0[/bold cyan]\n"
        "[green]Python Network Packet Analyzer[/green]",
        border_style="cyan",
    )