from time import sleep

from ui.dashboard import Dashboard


dashboard = Dashboard()

with dashboard.start():

    for i in range(20):

        dashboard.add_packet(
            {
                "time": f"12:00:{i:02}",
                "source": "192.168.1.14",
                "destination": "8.8.8.8",
                "protocol": "DNS",
                "source_port": "52344",
                "destination_port": "53",
                "size": "92",
            }
        )

        dashboard.refresh()

        sleep(0.5)