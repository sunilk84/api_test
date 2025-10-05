import random

import pytest
from utils.http_utils import HttpClient

@pytest.fixture(scope="session")
def base_url():
    return "https://api.restful-api.dev"

@pytest.fixture(scope="session")
def http_client(base_url):
    return HttpClient(base_url)

@pytest.fixture
def created_object_id(http_client):
    payload_post = {
        "name": "Apple MacBook Pro series 16",
        "data": {
            "year": 2025,
            "price": 1949.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = http_client.post("objects", json=payload_post, headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    return response.json()["id"]
