from todo_app.view_model import ViewModel

items = [   
    { '_id': '1', 'title': 'Test title 1', 'list_name': 'To Do' },
    { '_id': '2', 'title': 'Test title 2', 'list_name': 'To Do' },
    { '_id': '3', 'title': 'Test title 3', 'list_name': 'In Progress' },
    { '_id': '4', 'title': 'Test title 4', 'list_name': 'Complete' },
    { '_id': '5', 'title': 'Test title 5', 'list_name': 'To Do' },
    { '_id': '6', 'title': 'Test title 6', 'list_name': 'Complete' },
    { '_id': '7', 'title': 'Test title 7', 'list_name': 'To Do' },
    { '_id': '8', 'title': 'Test title 8', 'list_name': 'In Progress' },
    { '_id': '9', 'title': 'Test title 9', 'list_name': 'In Progress' },
    { '_id': '10', 'title': 'Test title 10', 'list_name': 'Complete' }
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


