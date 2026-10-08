import time
import psutil

from network import get_network_stats
from system import get_system_info


_previous_sent = None
_previous_received = None
_previous_time = None


def calculate_network_speed():
    global _previous_sent
    global _previous_received
    global _previous_time

    stats = get_network_stats()

    current_sent = stats["bytes_sent"]
    current_received = stats["bytes_received"]
    current_time = time.time()

    upload_speed = 0
    download_speed = 0

    if _previous_time is not None:
        elapsed = current_time - _previous_time

        if elapsed > 0:
            upload_speed = (
                current_sent - _previous_sent
            ) / elapsed

            download_speed = (
                current_received - _previous_received
            ) / elapsed

    _previous_sent = current_sent
    _previous_received = current_received
    _previous_time = current_time

    return {
        "upload_speed": round(max(upload_speed, 0), 2),
        "download_speed": round(max(download_speed, 0), 2)
    }


def get_system_stats():
    system = get_system_info()
    network = get_network_stats()
    speed = calculate_network_speed()

    return {
        **system,
        **network,
        **speed
    }


def get_processes(limit=10):
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "cpu_percent", "memory_percent"]
    ):
        try:
            info = process.info

            processes.append({
                "pid": info["pid"],
                "name": info["name"] or "Unknown",
                "cpu_percent": round(info["cpu_percent"] or 0, 2),
                "memory_percent": round(
                    info["memory_percent"] or 0, 2
                )
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(
        key=lambda item: item["cpu_percent"],
        reverse=True
    )

    return processes[:limit]
