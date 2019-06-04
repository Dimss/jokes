import requests
import os
from flask import Flask, jsonify

static_path = "{path}/public/".format(path=os.path.dirname(__file__))
app = application = Flask(__name__, static_folder=os.path.abspath(static_path))


@app.route('/api/jokes')
def hello_world():
    return jsonify(requests.get("https://api.chucknorris.io/jokes/random").json())


@app.route('/ui')
def root():
    return app.send_static_file('index.html')
