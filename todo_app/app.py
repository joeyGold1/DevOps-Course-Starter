from flask import Flask, redirect, render_template, request
from todo_app.data.errors import TrelloApiError
from todo_app.data.trello_items_service import add_item, get_item, get_items, remove_item, save_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    not_started_items = [item for item in items if item["status"]=="Not Started"]
    complete_items = [item for item in items if item["status"]=="Complete"]
    return render_template('index.html', not_started_items=not_started_items, complete_items=complete_items)

@app.route('/add', methods=["POST"])
def add():
    new_item = request.form.get('item_title')
    add_item(new_item)
    return redirect('/')

@app.route('/complete', methods=["POST"])
def complete():
    item_to_toggle = get_item(request.form.get('itemId'))
    item_to_toggle['status'] = 'Complete' 
    save_item(item_to_toggle)
    return redirect('/')

@app.route('/uncomplete', methods=["POST"])
def uncomplete():
    item_to_toggle = get_item(request.form.get('itemId'))
    item_to_toggle['status'] = 'Not Started'
    save_item(item_to_toggle)
    return redirect('/')

@app.route('/remove', methods=['POST'])
def remove():
    itemId = request.form.get('itemId')
    remove_item(itemId)
    return redirect('/')

@app.errorhandler(TrelloApiError)
def handle_trello_api_error(e):
    print(e)
    return redirect('/')