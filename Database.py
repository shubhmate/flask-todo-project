from flask import request, redirect
from pymongo import MongoClient

# Setup MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["items"]

@app.route('/submit_todoitem', methods=['POST'])
def submit_todo():
    # Get data from the form
    name = request.form.get('item_name')
    description = request.form.get('item_description')

    # Store in MongoDB using insert_one
    collection.insert_one({
        "item_name": name,
        "item_description": description
    })

    return "Item saved successfully!", 201
