from fastapi.testclient import TestClient

from .main import app

device = TestClient(app)


def test_create_device():
    response = device.post(
        "/api/v1/devices",
        json={
            "doorbot_id": 1,
            "doorbot_type": "cocoa_camera",
            "firmware_version": "cam-1.20"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "doorbot_id": 1,
        "online_status": False,
        "doorbot_type": "cocoa_camera",
        "firmware_version": "cam-1.20",
    }


def test_create_existing_device():
    response = device.post(
        "/api/v1/devices",
        json={
            "doorbot_id": 1,
            "doorbot_type": "cocoa_camera",
            "firmware_version": "cam-1.20"
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Camera already registered for this doorbot id"}


def test_read_device():
    response = device.get("/api/v1/devices/1")
    assert response.status_code == 200
    assert response.json() == {
        "doorbot_id": 1,
        "online_status": False,
        "doorbot_type": "cocoa_camera",
        "firmware_version": "cam-1.20",
    }

def test_read_devices():
    response = device.get("/api/v1/devices")
    assert response.status_code == 200


def test_put_device():
    response = device.put(
        "/api/v1/devices/1",
        json={

            "firmware_version": "mac-2.10",
            "online_status": True
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "doorbot_id": 1,
        "online_status": True,
        "doorbot_type": "cocoa_camera",
        "firmware_version": "mac-2.10",
    }


def test_delete_device():
    response = device.delete(
        "/api/v1/devices/1",
    )
    assert response.status_code == 200
    assert response.json() == {"detail": "Device with id 1 successfully deleted"}


def test_put_inexistent_device():
    response = device.put(
        "/api/v1/devices/1",
        json={

            "firmware_version": "mac-2.10",
            "online_status": True
        },
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Camera not found"}


def test_delete_inexisting_device():
    response = device.delete(
        "/api/v1/devices/1",
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Camera not found"}


def test_read_inexistent_device():
    response = device.get("/api/v1/devices/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Camera not found"}
