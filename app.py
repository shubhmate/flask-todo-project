import json
from flask import Flask, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Helper function to read the backend file
def read_backend_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "Data file not found"}

@app.route('/api', methods=['GET'])
def get_data():
    # Read data from the backend file
    data = read_backend_data()
    # Return the data as a JSON response
    return jsonify(data)

@app.route('/')
def todo_page():
    return render_template('todo.html')

if __name__ == '__main__':
    app.run(debug=True)




