import psutil
import socket
import time

_last_sent = None
_last_received = None
_last_time = None


def get_local_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except Exception:
        return "Unavailable"


def get_network_connections():
    connections = []

    try:
        for connection in psutil.net_connections(kind="inet"):
            if connection.status != psutil.CONN_NONE:
                local_address = "N/A"
                remote_address = "N/A"

                if connection.laddr:
                    local_address = (
                        f"{connection.laddr.ip}:{connection.laddr.port}"
                    )

                if connection.raddr:
                    remote_address = (
                        f"{connection.raddr.ip}:{connection.raddr.port}"
                    )

                connections.append({
                    "protocol": "TCP/UDP",
                    "local": local_address,
                    "remote": remote_address,
                    "status": connection.status,
                    "pid": connection.pid
                })

    except (psutil.AccessDenied, PermissionError):
        pass
    except Exception:
        pass

    return connections[:50]


def get_system_stats():
    global _last_sent
    global _last_received
    global _last_time

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    network = psutil.net_io_counters()

    current_time = time.time()

    upload_speed = 0
    download_speed = 0

    if _last_time is not None:
        elapsed = current_time - _last_time

        if elapsed > 0:
            upload_speed = (
                network.bytes_sent - _last_sent
            ) / elapsed

            download_speed = (
                network.bytes_recv - _last_received
            ) / elapsed

    _last_sent = network.bytes_sent
    _last_received = network.bytes_recv
    _last_time = current_time

    return {
        "cpu_percent": psutil.cpu_percent(interval=0.2),
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "hostname": socket.gethostname(),
        "local_ip": get_local_ip(),
        "bytes_sent": network.bytes_sent,
        "bytes_received": network.bytes_recv,
        "upload_speed": round(upload_speed, 2),
        "download_speed": round(download_speed, 2)
    }
