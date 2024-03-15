from todo_app.data.to_do_item import Item
from todo_app.view_model import ViewModel

items = [Item('1', 'Test title 1', 'To Do'),
            Item('2', 'Test title 2', 'To Do'),
            Item('3', 'Test title 3', 'Complete'),
            Item('4', 'Test title 4', 'To Do'),
            Item('5', 'Test title 5', 'Complete'),
            Item('6', 'Test title 6', 'To Do')
        ]

def test_view_model_complete_items_property():
    # Arrange
    view_model = ViewModel(items)

    # Act
    complete_items = view_model.complete_items

    # Assert
    assert items[2] in complete_items
    assert items[4] in complete_items
    assert not items[0] in complete_items
    assert not items[1] in complete_items
    assert not items[3] in complete_items
    assert not items[5] in complete_items

def test_view_model_complete_items_property():
    # Arrange
    view_model = ViewModel(items)

    # Act
    complete_items = view_model.not_started_items

    # Assert
    assert not items[2] in complete_items
    assert not items[4] in complete_items
    assert items[0] in complete_items
    assert items[1] in complete_items
    assert items[3] in complete_items
    assert items[5] in complete_items


