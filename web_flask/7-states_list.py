#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask, escape, render_template
from models import storage

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


@app.route('/number_odd_or_even/<int:n>/', strict_slashes=False)
def number_odd_or_even(n):
    ''' renders a message with a q param
        and displays value only if n is an integer
        renders an tml template
    '''
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' displays a list of all State
        objects present in DBStorage sorted by name
        renders an html template
    '''
    states_objs = storage.all('State').values()
    return render_template('7-states_list.html', states=states_objs)


@app.teardown_appcontext
def close_session_db(exit):
    ''' remove the current SQLAlchemy Session '''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
