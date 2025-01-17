class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def not_started_items(self):
        return [item for item in self._items if item['list_name'] == "To Do"]

    @property
    def in_progress_items(self):
        return [item for item in self._items if item['list_name'] == "In Progress"]

    @property
    def complete_items(self):
        return [item for item in self._items if item['list_name'] == "Complete"]
