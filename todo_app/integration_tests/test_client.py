from dotenv import load_dotenv, find_dotenv
import pytest
import requests
import os
from todo_app import app

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data
    
    def json(self):
        return self.fake_response_data

def stub(method, url, params={}):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')
    if method == 'GET' and url == f'https://api.trello.com/1/boards/{test_board_id}/cards':
        fake_response_data = [{
            "id": "id-1","checkItemStates": [],
            "idList": "test_not_started_list_id",
            "name": "Test card",
        }]
        return StubResponse(fake_response_data)

    if method == 'POST' and url == f'https://api.trello.com/1/cards':
        fake_response_data = {
            "id": "id-2","checkItemStates": [],
            "idList": "test_not_started_list_id",
            "name": "Test card2",
        }
        return StubResponse(fake_response_data)
    
    raise Exception(f'Integration test did not expect URL "{url}"')

def test_index_page(monkeypatch, client):
    # Arrange
    monkeypatch.setattr(requests, 'request', stub)

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == 200
    assert 'Test card' in response.data.decode()

def test_create_card(monkeypatch, client):
    # Arrange
    monkeypatch.setattr(requests, 'request', stub)

    # Act
    response = client.post('/add', data={ "item_title": "Test card2" })

    # Assert
    assert response.status_code == 302
