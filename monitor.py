import psutil
import socket
import time


last_sent = 0
last_received = 0
last_time = time.time()


def get_local_ip():
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception:
        return "Unavailable"


def get_network_connections():
    connections = []

    try:
        for connection in psutil.net_connections(kind="inet"):
            if connection.status == "ESTABLISHED":
                local_address = (
                    f"{connection.laddr.ip}:{connection.laddr.port}"
                    if connection.laddr
                    else "Unknown"
                )

                remote_address = (
                    f"{connection.raddr.ip}:{connection.raddr.port}"
                    if connection.raddr
                    else "Unknown"
                )

                connections.append({
                    "protocol": "TCP",
                    "local": local_address,
                    "remote": remote_address,
                    "status": connection.status,
                    "pid": connection.pid
                })

    except (psutil.AccessDenied, PermissionError):
        pass

    return connections[:50]


def get_system_stats():
    global last_sent, last_received, last_time

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    network = psutil.net_io_counters()

    current_time = time.time()
    elapsed = current_time - last_time

    upload_speed = 0
    download_speed = 0

    if elapsed > 0 and last_sent != 0:
        upload_speed = (network.bytes_sent - last_sent) / elapsed
        download_speed = (network.bytes_recv - last_received) / elapsed

    last_sent = network.bytes_sent
    last_received = network.bytes_recv
    last_time = current_time

    return {
        "cpu_percent": psutil.cpu_percent(interval=0.2),
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "hostname": socket.gethostname(),
        "local_ip": get_local_ip(),
        "bytes_sent": network.bytes_sent,
        "bytes_received": network.bytes_recv,
        "upload_speed": upload_speed,
        "download_speed": download_speed
    }
