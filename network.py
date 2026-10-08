import socket

import psutil


def get_local_ip():
    """Return the local machine IP address."""

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.connect(("8.8.8.8", 80))
        return sock.getsockname()[0]

    except OSError:
        return "Unavailable"

    finally:
        sock.close()


def get_network_stats():
    """Return network traffic statistics."""

    counters = psutil.net_io_counters()

    return {
        "local_ip": get_local_ip(),
        "bytes_sent": counters.bytes_sent,
        "bytes_received": counters.bytes_recv,
        "packets_sent": counters.packets_sent,
        "packets_received": counters.packets_recv
    }


def get_interfaces():
    """Return available network interfaces and their addresses."""

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
    """Return active network connections."""

    connections = []

    try:
        system_connections = psutil.net_connections(
            kind="inet"
        )

        for connection in system_connections:

            if connection.status == psutil.CONN_NONE:
                continue

            local = "N/A"
            remote = "N/A"

            if connection.laddr:
                local = (
                    f"{connection.laddr.ip}:"
                    f"{connection.laddr.port}"
                )

            if connection.raddr:
                remote = (
                    f"{connection.raddr.ip}:"
                    f"{connection.raddr.port}"
                )

            connections.append({
                "local": local,
                "remote": remote,
                "status": connection.status,
                "pid": connection.pid
            })

    except (psutil.AccessDenied, PermissionError):
        pass

    return connections[:limit]
