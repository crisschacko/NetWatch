import psutil
import socket


def get_cpu_usage():
    return psutil.cpu_percent(interval=0.2)


def get_memory_usage():
    return psutil.virtual_memory().percent


def get_disk_usage():
    return psutil.disk_usage("/").percent


def get_hostname():
    return socket.gethostname()


def get_system_info():
    return {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "hostname": get_hostname()
    }
