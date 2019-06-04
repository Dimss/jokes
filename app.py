import requests
import os
from flask import Flask, jsonify

app = application = Flask(__name__, static_folder=os.path.abspath('/Users/dima/code/pycon19-workshop/app/public/'))


@app.route('/api/jokes')
def hello_world():
    return jsonify(requests.get("https://api.chucknorris.io/jokes/random").json())


@app.route('/ui')
def root():
    return app.send_static_file('index.html')
