class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def not_started_items(self):
        return []

    @property
    def complete_items(self):
        return []
