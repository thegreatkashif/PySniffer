from rich.panel import Panel


def footer():

    return Panel.fit(
        "[yellow]"
        "CTRL+C : Stop Capture    "
        "F : Filter    "
        "S : Save    "
        "TAB : Statistics"
        "[/yellow]",
        border_style="yellow",
    )