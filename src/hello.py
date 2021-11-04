"""
set FLASK_APP=./src/hello.py
flask run

"""

import flask

app = flask.Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"
