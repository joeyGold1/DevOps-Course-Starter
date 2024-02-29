from todo_app.data import trello_utils


class Item:
    def __init__(self, id, title, status="To Do"):
        self.id = id
        self.title = title
        self.status = status
    
    def to_trello_card(self):
        return {
            "id": self.id,
            "name": self.title,
            "idList": trello_utils.status_to_id[self.status]
        }

    @classmethod
    def from_trello_card(cls, trello_item):
        return cls(trello_item["id"], trello_item["name"], trello_utils.id_to_status[trello_item["idList"]])