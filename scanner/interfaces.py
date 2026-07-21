from scapy.all import get_if_list
from scapy.arch.windows import get_windows_if_list


def list_interfaces():

    interfaces = []

    try:

        windows_interfaces = get_windows_if_list()

        for interface in windows_interfaces:

            interfaces.append({
                "name": interface.get("name", "Unknown"),
                "description": interface.get("description", ""),
                "guid": interface.get("guid", ""),
            })

        return interfaces

    except Exception:

        return [
            {
                "name": iface,
                "description": "",
                "guid": ""
            }
            for iface in get_if_list()
        ]