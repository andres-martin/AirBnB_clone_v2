#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    ''' renders a message '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' renders a message '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_param(text):
    ''' renders a message with a q param '''
    return "C %s" % escape(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
