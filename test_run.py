import pytest
from run import app

@pytest.fixture
def client():
    app.testing = True
    client = app.test_client()
    yield client

def test_random_number(client):
    res = client.get('/api/random')
    assert res.status_code == 200

