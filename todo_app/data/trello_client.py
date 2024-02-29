import os
import requests
from todo_app.data.errors import TrelloApiError

trello_base_url = "https://api.trello.com/1"

board_id = os.getenv("TRELLO_BOARD_ID")
trello_api_key = os.getenv("TRELLO_API_KEY")
trello_api_token = os.getenv("TRELLO_API_TOKEN")

authentication_params = {
    "key": trello_api_key,
    "token": trello_api_token
}

trello_params = {
    "fields": ["id", "name", "idList"]
}

def get_items():
    path = "/boards/{id}/cards".format(id = board_id)
    return make_trello_request(path)

def get_item(card_id):
    path = "/cards/{id}".format(id = card_id)
    return make_trello_request(path)

def get_lists():
    path = "/boards/{id}/lists".format(id = board_id)
    return make_trello_request(path)

def get_list(list_id):
    path = "/lists/{id}".format(id=list_id)
    return make_trello_request(path)

def create_item(title, list_id):
    path = "/cards"
    create_item_params = {"name": title, "idList": list_id}
    return make_trello_request(path, "POST", create_item_params)
    
def update_item(trello_item):
    path = "/cards/{id}".format(id=trello_item['id'])
    return make_trello_request(path, "PUT", trello_item)

def delete_item(item_id):
    path = "/cards/{id}".format(id=item_id)
    return make_trello_request(path, "DELETE")

def make_trello_request(path, request_method = "GET", request_params = {}):
    response = requests.request(
        request_method,
        trello_base_url + path,
        params = authentication_params | trello_params | request_params
    )
    try:
        return response.json()
    except:
        raise TrelloApiError(response.text, path, request_method) 
