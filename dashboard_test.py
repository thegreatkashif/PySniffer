from time import sleep

from rich.live import Live

from ui.dashboard import Dashboard


dashboard = Dashboard()

stats = {
    "packets": 0,
    "bytes": 0,
    "duration": 0,
    "pps": 0,
    "bps": 0,
    "protocols": {},
    "sources": {},
    "destinations": {},
}


with dashboard.start() as live:

    for i in range(100):

        packet = {
            "time": f"12:00:{i:02}",
            "source": f"192.168.1.{i % 10}",
            "destination": "8.8.8.8",
            "protocol": "HTTPS",
            "source_port": 50000 + i,
            "destination_port": 443,
            "size": 1500,
        }

        stats["packets"] += 1
        stats["bytes"] += packet["size"]
        stats["duration"] += 0.2
        stats["pps"] = stats["packets"] / max(stats["duration"], 1)

        stats["protocols"]["HTTPS"] = stats["packets"]

        dashboard.update(packet, stats)

        live.update(dashboard.layout)

        sleep(0.05)