import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_add(client):
    response = client.get('/add/2/3')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 5

def test_simple():
    assert 1 + 1 == 2