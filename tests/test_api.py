from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_system_api():
    client = app.test_client()

    response = client.get("/api/system")

    assert response.status_code == 200
    assert response.is_json


def test_network_api():
    client = app.test_client()

    response = client.get("/api/network")

    assert response.status_code == 200
    assert response.is_json


def test_process_api():
    client = app.test_client()

    response = client.get("/api/processes")

    assert response.status_code == 200
    assert response.is_json


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "online"
