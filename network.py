import socket

import psutil


def get_local_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.connect(("8.8.8.8", 80))
        return sock.getsockname()[0]
    except OSError:
        return "Unavailable"
    finally:
        sock.close()


def get_network_stats():
    counters = psutil.net_io_counters()

    return {
        "local_ip": get_local_ip(),
        "bytes_sent": counters.bytes_sent,
        "bytes_received": counters.bytes_recv,
        "packets_sent": counters.packets_sent,
        "packets_received": counters.packets_recv
    }


def get_interfaces():
    interfaces = {}

    for name, addresses in psutil.net_if_addrs().items():
        interfaces[name] = []

        for address in addresses:
            interfaces[name].append({
                "family": str(address.family),
                "address": address.address,
                "netmask": address.netmask
            })

    return interfaces


def get_connections(limit=50):
    connections = []

    try:
        for connection in psutil.net_connections(kind="inet"):
            if connection.status == psutil.CONN_NONE:
                continue

            local = "N/A"
            remote = "N/A"

            if connection.laddr:
                local = f"{connection.laddr.ip}:{connection.laddr.port}"

            if connection.raddr:
                remote = f"{connection.raddr.ip}:{connection.raddr.port}"

            connections.append({
                "local": local,
                "remote": remote,
                "status": connection.status,
                "pid": connection.pid
            })

    except (psutil.AccessDenied, PermissionError):
        pass

    return connections[:limit]
