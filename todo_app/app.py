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

@app.route('/complete', methods=["POST"])
def complete():
    item_to_mark_complete = trello_items_service.get_item(request.form.get('itemId'))
    item_to_mark_complete.status = 'Complete' 
    trello_items_service.save_item(item_to_mark_complete)
    return redirect('/')

@app.route('/uncomplete', methods=["POST"])
def uncomplete():
    item_to_mark_to_do = trello_items_service.get_item(request.form.get('itemId'))
    item_to_mark_to_do.status = 'Not Started'
    trello_items_service.save_item(item_to_mark_to_do)
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