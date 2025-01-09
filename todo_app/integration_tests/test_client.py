from dotenv import load_dotenv, find_dotenv
import pytest
import requests
import os
from todo_app import app

import mongomock

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

def test_create_card(client):
    # Act
    response = client.post('/add', data={ "item_title": "Test card2" })

    # Assert
    assert response.status_code == 302

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == 200
    assert 'Test card' in response.data.decode()
