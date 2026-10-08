from network import (
    get_local_ip,
    get_network_stats,
    get_connections
)


def test_local_ip():
    ip = get_local_ip()

    assert isinstance(ip, str)
    assert len(ip) > 0


def test_network_stats():
    stats = get_network_stats()

    assert "local_ip" in stats
    assert "bytes_sent" in stats
    assert "bytes_received" in stats


def test_connections():
    connections = get_connections()

    assert isinstance(connections, list)
