from scanner.statistics import Statistics


def test_statistics_update():

    stats = Statistics()

    packet = {
        "size": 100,
        "protocol": "TCP",
        "source": "1.1.1.1",
        "destination": "2.2.2.2",
    }

    stats.update(packet)

    assert stats.total_packets == 1
    assert stats.total_bytes == 100