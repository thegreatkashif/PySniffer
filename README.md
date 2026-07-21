# PySniffer

A modern Python packet analyzer built with Scapy and Rich.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Status](https://img.shields.io/badge/Status-Stable-success)

---

## Features

- Live packet capture
- Live Rich dashboard
- Interface discovery
- Protocol filtering
- JSON export
- CSV export
- PCAP export
- Offline PCAP analysis
- Reverse DNS lookup
- Protocol statistics
- Top talkers
- Thread-safe dashboard
- Cross-platform

---


## Installation

```bash
git clone https://github.com/thegreatkashif/PySniffer.git

cd PySniffer

pip install -r requirements.txt
```

---

## Usage

Capture 100 packets

```bash
python pysniffer.py --count 100
```

Capture only DNS

```bash
python pysniffer.py --filter dns
```

Capture HTTPS

```bash
python pysniffer.py --filter https
```

Export JSON

```bash
python pysniffer.py --json packets.json
```

Export CSV

```bash
python pysniffer.py --csv packets.csv
```

Export PCAP

```bash
python pysniffer.py --pcap capture.pcap
```

Analyze PCAP

```bash
python pysniffer.py --pcap-read capture.pcap
```

List interfaces

```bash
python pysniffer.py --list-interfaces
```

List filters

```bash
python pysniffer.py --list-filters
```

---

## Supported Filters

- arp
- tcp
- udp
- icmp
- dns
- dhcp
- ssh
- ftp
- smtp
- pop3
- imap
- http
- https
- mysql
- postgres
- redis
- ntp
- snmp
- mdns
- quic
- rdp

---

## Built With

- Python
- Scapy
- Rich
- Colorama

---

## License

MIT License