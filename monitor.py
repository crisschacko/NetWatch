import psutil
import socket


def get_system_stats():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "hostname": socket.gethostname(),
        "local_ip": socket.gethostbyname(socket.gethostname())
    }
