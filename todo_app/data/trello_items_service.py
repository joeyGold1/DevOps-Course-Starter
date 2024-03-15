from todo_app.data.trello_client import TrelloClient
from todo_app.data.trello_utils import TrelloUtils
from todo_app.data.to_do_item import Item
class TrelloItemsService:
    def __init__(self):
        self.trello_client = TrelloClient()
        self.trello_utils = TrelloUtils()

    def get_items(self):
        """
        Fetches all saved items from trello.

        Returns:
            list: The list of saved items.
        """
        trello_items = self.trello_client.get_items()

        items = list(map(Item.from_trello_card, trello_items, [self.trello_utils for _ in trello_items]))
        return items

    def get_item(self, id):
        """
        Fetches the saved item with the specified ID.

        Args:
            id: The ID of the item.

        Returns:
            item: The saved item, or None if no items match the specified ID.
        """
        trello_item = self.trello_client.get_item(id)
        return Item.from_trello_card(trello_item, self.trello_utils)


    def add_item(self, title):
        """
        Adds a new item with the specified title to the trello board.

        Args:
            title: The title of the item.

        Returns:
            item: The saved item.
        """
        list_id = self.trello_utils.status_to_id["Not Started"]

        trello_item = self.trello_client.create_item(title, list_id)

        return Item.from_trello_card(trello_item, self.trello_utils)


    def save_item(self, item):
        """
        Updates an existing item in the trello. If no existing item matches the ID of the specified item, nothing is saved.

        Args:
            item: The item to save.
        """
        trello_item = item.to_trello_card()
        updated_item = Item.from_trello_card(self.trello_client.update_item(trello_item), self.trello_utils)

        return updated_item

    def remove_item(self, id):
        """
        Removes an existing item from the trello board. If no existing item matches the ID of the specified item, nothing is removed.

        Args:
            id: The ID of the item to remove.
        """
        
        self.trello_client.delete_item(id)
