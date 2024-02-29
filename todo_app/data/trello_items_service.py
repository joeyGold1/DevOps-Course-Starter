from todo_app.data import trello_client
from todo_app.data import trello_utils
from todo_app.data.to_do_item import Item

def get_items():
    """
    Fetches all saved items from trello.

    Returns:
        list: The list of saved items.
    """
    trello_items = trello_client.get_items()

    items = list(map(Item.from_trello_card, trello_items))
    return items

def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    trello_item = trello_client.get_item(id)
    return Item.from_trello_card(trello_item)


def add_item(title):
    """
    Adds a new item with the specified title to the trello board.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    list_id = trello_utils.status_to_id["Not Started"]

    trello_item = trello_client.create_item(title, list_id)

    return Item.from_trello_card(trello_item)


def save_item(item):
    """
    Updates an existing item in the trello. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    trello_item = item.to_trello_card()
    updated_item = Item.from_trello_card(trello_client.update_item(trello_item))

    return updated_item

def remove_item(id):
    """
    Removes an existing item from the trello board. If no existing item matches the ID of the specified item, nothing is removed.

    Args:
        id: The ID of the item to remove.
    """
    
    trello_client.delete_item(id)
