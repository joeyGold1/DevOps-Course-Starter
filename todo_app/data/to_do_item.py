from todo_app.data.trello_utils import TrelloUtils


class Item:
    def __init__(self, id, title, status="To Do", trello_utils = TrelloUtils()):
        self.id = id
        self.title = title
        self.status = status
        self.trello_utils = trello_utils
    
    def to_trello_card(self):
        return {
            "id": self.id,
            "name": self.title,
            "idList": self.trello_utils.status_to_id[self.status]
        }

    @classmethod
    def from_trello_card(cls, trello_item, trello_utils = TrelloUtils()):
        return cls(trello_item["id"], trello_item["name"], trello_utils.id_to_status[trello_item["idList"]], trello_utils)