from flask.testing import FlaskClient
import pytest
from backend.app import app
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_webhook(client: FlaskClient):
    """Test the /webhook endpoint with a sample message."""
    response = client.post('/webhook', json={"message": "What is Python?"})
    json_data = response.get_json()
    assert response.status_code == 200
    assert "This is a placeholder response for the message" in json_data['message']

def test_webhook():
    tester = app.test_client()
    response = tester.post('/webhook', data=json.dumps({'message': 'Hello'}), content_type='application/json')
    assert response.status_code == 200
    response_json = response.get_json()
    print("Response JSON:", response_json)
    assert 'status' in response_json
    assert response_json['status'] == 'processing'
    assert 'task_id' in response_json