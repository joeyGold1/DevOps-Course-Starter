from flask import Flask, redirect, render_template, request
from todo_app.data.errors import TrelloApiError
from todo_app.data.trello_items_service import TrelloItemsService

from todo_app.flask_config import Config
from todo_app.view_model import ViewModel

app = Flask(__name__)
app.config.from_object(Config())
trello_items_service = TrelloItemsService()

@app.route('/')
def index():
    items = trello_items_service.get_items()
    items_view_model = ViewModel(items)
    return render_template('index.html', view_model=items_view_model)

@app.route('/add', methods=["POST"])
def add():
    new_item_title = request.form.get('item_title')
    trello_items_service.add_item(new_item_title)
    return redirect('/')

@app.route('/mark/<status>', methods=["POST"])
def mark_status(status):
    item_to_mark_status = trello_items_service.get_item(request.form.get('itemId'))
    status_to_mark = {"complete": "Complete", "to_do": "To Do", "in_progress": "In Progress"}[status]
    item_to_mark_status.status = status_to_mark
    trello_items_service.save_item(item_to_mark_status)
    return redirect('/')


@app.route('/remove', methods=['POST'])
def remove():
    itemId = request.form.get('itemId')
    trello_items_service.remove_item(itemId)
    return redirect('/')

@app.errorhandler(TrelloApiError)
def handle_trello_api_error(e):
    print(e)
    return redirect('/')