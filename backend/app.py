from flask import Flask, request
import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

import json

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client.test2
collection = db['flask-t']

app = Flask(__name__)



@app.route('/api', methods=['GET'])
def api():
    with open('api.json') as f:
        data = json.load(f)
    return data

@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form.get('name')
    form_data = dict(request.json)
    collection.insert_one(form_data)
    return "Hi " + name + "!"

@app.route('/view')
def view():
    data = collection.find()
    data = list(data)

    for item in data:
        print(item)
        del item['_id']
    data = {
        'data':data
    }

    return data

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=9000, debug=True)