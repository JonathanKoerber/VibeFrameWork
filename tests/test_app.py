import pytest
from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_home_lists_routes(client):
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["message"] == "cs504-ai Flask demo"
    assert "/health" in data["routes"]


def test_info_returns_item(client):
    resp = client.get("/info/widget")
    assert resp.status_code == 200
    assert resp.get_json()["item"] == "widget"


def test_echo_round_trips_payload(client):
    resp = client.post("/echo", json={"message": "HI"})
    assert resp.status_code == 200
    assert resp.get_json()["echo"]["message"] == "HI"
