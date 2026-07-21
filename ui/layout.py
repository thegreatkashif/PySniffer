from rich.layout import Layout


def make_layout():

    layout = Layout()

    layout.split_column(
        Layout(name="header", size=5),
        Layout(name="body"),
        Layout(name="footer", size=5),
    )

    return layout