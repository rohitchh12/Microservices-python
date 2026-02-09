from flask import Flask, render_template, request
from datetime import datetime
import requests

BACKEND_URI = 'http://0.0.0.0:9000'

app = Flask(__name__)
@app.route('/')
def home():
    now = datetime.now()
    formatted_time = now.strftime("%A, %H:%M:%S")
    return render_template('index.html', time = formatted_time)

@app.route('/submit', methods = ['POST'])
def submit():
    form_data = dict(request.form)

    requests.post(BACKEND_URI + "/submit" , json=form_data)
    return "Data submitted successfully!"

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=8000, debug=True)