from flask import Flask, redirect, render_template, request
from todo_app.data.trello_items_service import add_item, get_item, get_items, remove_item, save_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = sorted(get_items(), key=lambda item: 1 if item['status'] == "Not Started" else 2)
    return render_template('index.html', items=items)

@app.route('/add', methods=["POST"])
def add():
    new_item = request.form.get('item_title')
    add_item(new_item)
    return redirect('/')

@app.route('/toggle', methods=["POST"])
def toggle_complete():
    item_to_toggle = get_item(request.form.get('itemId'))
    item_to_toggle['status'] = 'Complete' if item_to_toggle['status'] == 'Not Started' else 'Not Started'
    save_item(item_to_toggle)
    return redirect('/')

@app.route('/remove', methods=['POST'])
def remove():
    itemId = request.form.get('itemId')
    remove_item(itemId)
    return redirect('/')
