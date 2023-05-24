from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

app = Flask(__name__)
username = urllib.parse.quote_plus('pp722qf')
password = urllib.parse.quote_plus('m%cv5kCF')
client = MongoClient(f'mongodb+srv://{username}:{password}@cluster0.nfkn6si.mongodb.net/?retryWrites=true&w=majority')
db = client.todo_app
collection = db.todos


@app.route('/')
def index():
    todos = collection.find({}).sort('priority', -1)
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    priority = int(request.form['priority'])
    collection.insert_one({'todo': todo, 'priority': priority})
    return redirect('/')


@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    collection.delete_one({'_id': ObjectId(id)})
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

