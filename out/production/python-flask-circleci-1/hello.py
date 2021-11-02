"""

To run the application
1. open a terminal
2. set FLASK_APP=./src/hello.py
3. flask run

"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
