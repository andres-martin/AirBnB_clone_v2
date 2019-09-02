#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask, escape, render_template
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


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>/', strict_slashes=False)
def python_param(text):
    ''' renders a message with a q param
        and defaults value
    '''
    return "Python %s" % escape(text.replace('_', ' '))


@app.route('/number/<int:n>/', strict_slashes=False)
def number_param(n):
    ''' renders a message with a q param
        and displays value only if n is an integer
    '''
    return "%d is a number" % n


@app.route('/number_template/<int:n>/', strict_slashes=False)
def number_template(n):
    ''' renders a message with a q param
        and displays value only if n is an integer
        renders an tml template
    '''
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
