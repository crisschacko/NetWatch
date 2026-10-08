from system import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_system_info
)


def test_cpu_usage():
    value = get_cpu_usage()
    assert 0 <= value <= 100


def test_memory_usage():
    value = get_memory_usage()
    assert 0 <= value <= 100


def test_disk_usage():
    value = get_disk_usage()
    assert 0 <= value <= 100


def test_system_info():
    info = get_system_info()

    assert "cpu_percent" in info
    assert "memory_percent" in info
    assert "disk_percent" in info
    assert "hostname" in info
    assert "platform" in info
