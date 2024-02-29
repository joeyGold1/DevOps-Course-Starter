import todo_app.data.trello_client as trello_client
import todo_app.data.trello_utils as trello_utils

def get_items():
    """
    Fetches all saved items from trello.

    Returns:
        list: The list of saved items.
    """
    trello_items = trello_client.get_items()

    items = map(map_trello_item_to_item, trello_items)

    return list(items)

def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    trello_item = trello_client.get_item(id)
    return map_trello_item_to_item(trello_item)


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

    return map_trello_item_to_item(trello_item)


def save_item(item):
    """
    Updates an existing item in the trello. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    
    trello_item = map_item_to_trello_item(item)
    updated_item = map_trello_item_to_item(trello_client.update_item(trello_item))

    return updated_item

def remove_item(id):
    """
    Removes an existing item from the trello board. If no existing item matches the ID of the specified item, nothing is removed.

    Args:
        id: The ID of the item to remove.
    """
    
    trello_client.delete_item(id)

map_trello_item_to_item = lambda trello_item: {
                    "id": trello_item["id"],
                    "title": trello_item["name"],
                    "status": trello_utils.id_to_status[trello_item["idList"]]
                }

map_item_to_trello_item = lambda item: {
    "id": item["id"],
    "name": item["title"],
    "idList": trello_utils.status_to_id[item["status"]]
}