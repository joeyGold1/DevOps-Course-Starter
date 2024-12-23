from flask import Flask, redirect, render_template, request, Response
from todo_app.data.errors import TrelloApiError
from todo_app.data.mongo_client import MongoClient
from todo_app.view_model import ViewModel

def create_app():
    app = Flask(__name__)
    mongo_client = MongoClient()

    @app.route('/')
    def index():
        items = mongo_client.get_items()
        items_view_model = ViewModel(items)
        return render_template('index.html', view_model=items_view_model)

    @app.route('/add', methods=["POST"])
    def add():
        new_item_title = request.form.get('item_title')
        mongo_client.create_item(new_item_title, 'To Do')
        return redirect('/')

    @app.route('/mark/<status>', methods=["POST"])
    def mark_status(status):
        status_to_mark = {"complete": "Complete", "to_do": "To Do", "in_progress": "In Progress"}[status]
        mongo_client.update_item_status(request.form.get('itemId'), status_to_mark)
        return redirect('/')


    @app.route('/remove', methods=['POST'])
    def remove():
        mongo_client.delete_item(request.form.get('itemId'))
        return redirect('/')

    return app