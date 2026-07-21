from scanner.exporter import Exporter


def test_exporter_add_packet():

    exporter = Exporter()

    exporter.add_packet(
        {"protocol": "TCP"}
    )

    assert len(exporter.packets) == 1