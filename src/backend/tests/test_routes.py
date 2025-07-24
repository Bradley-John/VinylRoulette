import pytest
from src.backend.app.app import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_spin_returns_200(client):
    with patch('routes.get_random_album') as mock_get_album:
        mock_get_album.return_value = {"artist": "Daft Punk", "album": "Discovery"}
        response = client.get('/spin')
        assert response.status_code == 200

def test_spin_returns_json_structure(client):
    with patch('routes.get_random_album') as mock_get_album:
        mock_get_album.return_value = {"artist": "Daft Punk", "album": "Discovery"}
        response = client.get('/spin')
        data = response.get_json()
        assert data == {"artist": "Daft Punk", "album": "Discovery"}
