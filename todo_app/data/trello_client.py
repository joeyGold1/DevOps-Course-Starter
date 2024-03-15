import os
import requests
from todo_app.data.errors import TrelloApiError

trello_base_url = "https://api.trello.com/1"

class  TrelloClient:
    def __init__(self):
        self.authentication_params = {
            "key": os.getenv("TRELLO_API_KEY"),
            "token": os.getenv("TRELLO_API_TOKEN")
        }
        self.board_id = os.getenv("TRELLO_BOARD_ID")
        self.trello_params = {
            "fields": ["id", "name", "idList"]
        }

    def get_items(self):
        path = "/boards/{id}/cards".format(id = self.board_id)
        return self.make_trello_request(path)

    def get_item(self, card_id):
        path = "/cards/{id}".format(id = card_id)
        return self.make_trello_request(path)

    def get_lists(self):
        path = "/boards/{id}/lists".format(id = self.board_id)
        return self.make_trello_request(path)

    def get_list(self, list_id):
        path = "/lists/{id}".format(id=list_id)
        return self.make_trello_request(path)

    def create_item(self, title, list_id):
        path = "/cards"
        create_item_params = {"name": title, "idList": list_id}
        return self.make_trello_request(path, "POST", create_item_params)
        
    def update_item(self, trello_item):
        path = "/cards/{id}".format(id=trello_item['id'])
        return self.make_trello_request(path, "PUT", trello_item)

    def delete_item(self, item_id):
        path = "/cards/{id}".format(id=item_id)
        return self.make_trello_request(path, "DELETE")

    def make_trello_request(self, path, request_method = "GET", request_params = {}):
        response = requests.request(
            request_method,
            trello_base_url + path,
            params = self.authentication_params | self.trello_params | request_params
        )
        try:
            return response.json()
        except:
            raise TrelloApiError(response.text, path, request_method) 
