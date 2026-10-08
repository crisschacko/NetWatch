import platform
import socket
import time

import psutil


def get_cpu_usage():
    return psutil.cpu_percent(interval=0.2)


def get_memory_usage():
    return psutil.virtual_memory().percent


def get_disk_usage(path="/"):
    try:
        return psutil.disk_usage(path).percent
    except OSError:
        return 0


def get_hostname():
    return socket.gethostname()


def get_platform():
    return f"{platform.system()} {platform.release()}"


def get_cpu_count():
    return psutil.cpu_count(logical=True) or 0


def get_uptime_seconds():
    return int(time.time() - psutil.boot_time())


def get_system_info():
    return {
        "cpu_percent": get_cpu_usage(),
        "memory_percent": get_memory_usage(),
        "disk_percent": get_disk_usage(),
        "hostname": get_hostname(),
        "platform": get_platform(),
        "cpu_count": get_cpu_count(),
        "uptime_seconds": get_uptime_seconds()
    }
