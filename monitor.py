import psutil
import socket


def get_system_stats():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    network = psutil.net_io_counters()

    return {
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "hostname": socket.gethostname(),
        "local_ip": get_local_ip(),
        "bytes_sent": network.bytes_sent,
        "bytes_received": network.bytes_recv
    }


def get_local_ip():
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception:
        return "Unavailable"
