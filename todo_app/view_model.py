class ViewModel:
    def __init__(self, not_started_items, complete_items):
        self._not_started_items= not_started_items
        self._complete_items= complete_items
 
    @property
    def not_started_items(self):
        return self._not_started_items

    @property
    def complete_items(self):
        return self._complete_items
