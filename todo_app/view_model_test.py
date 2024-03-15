from todo_app.data.to_do_item import Item
from todo_app.view_model import ViewModel

items = [Item('1', 'Test title 1', 'To Do'),
            Item('2', 'Test title 2', 'To Do'),
            Item('3', 'Test title 3', 'In Progress'),
            Item('4', 'Test title 4', 'Complete'),
            Item('5', 'Test title 5', 'To Do'),
            Item('6', 'Test title 6', 'Complete'),
            Item('7', 'Test title 7', 'To Do'),
            Item('8', 'Test title 8', 'In Progress'),
            Item('9', 'Test title 9', 'In Progress'),
            Item('10', 'Test title 10', 'Complete')
        ]

def test_view_model_complete_items_property():
    # Arrange
    view_model = ViewModel(items)

    # Act
    complete_items = view_model.complete_items

    # Assert
    assert not items[0] in complete_items
    assert not items[1] in complete_items
    assert not items[2] in complete_items
    assert items[3] in complete_items
    assert not items[4] in complete_items
    assert items[5] in complete_items
    assert not items[6] in complete_items
    assert not items[7] in complete_items
    assert not items[8] in complete_items
    assert items[9] in complete_items

def test_view_model_in_progress_items_property():
    # Arrange
    view_model = ViewModel(items)

    # Act
    in_progress_items = view_model.in_progress_items

    # Assert
    assert not items[0] in in_progress_items
    assert not items[1] in in_progress_items
    assert items[2] in in_progress_items
    assert not items[3] in in_progress_items
    assert not items[4] in in_progress_items
    assert not items[5] in in_progress_items
    assert not items[6] in in_progress_items
    assert items[7] in in_progress_items
    assert items[8] in in_progress_items
    assert not items[9] in in_progress_items

def test_view_model_to_do_items_property():
    # Arrange
    view_model = ViewModel(items)

    # Act
    not_started_items = view_model.not_started_items

    # Assert
    assert items[0] in not_started_items
    assert items[1] in not_started_items
    assert not items[2] in not_started_items
    assert not items[3] in not_started_items
    assert items[4] in not_started_items
    assert not items[5] in not_started_items
    assert items[6] in not_started_items
    assert not items[7] in not_started_items
    assert not items[8] in not_started_items
    assert not items[9] in not_started_items


