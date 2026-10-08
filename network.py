import psutil
import socket


def get_local_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except Exception:
        return "Unavailable"


def get_network_stats():
    network = psutil.net_io_counters()

    return {
        "bytes_sent": network.bytes_sent,
        "bytes_received": network.bytes_recv,
        "local_ip": get_local_ip()
    }


def get_connections():
    connections = []

    try:
        for connection in psutil.net_connections(kind="inet"):

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

    return connections[:50]
