import os
from bson.objectid import ObjectId
import pymongo
from todo_app.data.errors import TrelloApiError

class MongoClient:
    def __init__(self):
        connection_string = os.getenv("MONGO_DB_CONNECTION_STRING")
        db_name = os.getenv("MONGO_DB_DB_NAME")
        collection_name = os.getenv("MONGO_DB_ITEMS_COLLECTION_NAME")

        self.client = pymongo.MongoClient(connection_string)
        db = self.client[db_name]
        self.collection = db[collection_name]

    def get_items(self):
        mongo_items = self.collection.find()
        items = []
        for item in mongo_items:
            items.append(item)
        return items

    def get_item(self, item_id):
        return self.collection.find_one({ '_id': ObjectId(item_id) })
    
    def create_item(self, title, list_name):
        create_item_params = { "title": title, "list_name": list_name}
        id = str(self.collection.insert_one(create_item_params).inserted_id)
        return { '_id': id, 'title': title, 'list_name': list_name }
        
    def update_item_status(self, item_id, new_list_name):
        return self.collection.update_one({ "_id": ObjectId(item_id) }, { "$set": {"list_name": new_list_name}})

    def delete_item(self, item_id):
        return self.collection.delete_one({ "_id": ObjectId(item_id) })
