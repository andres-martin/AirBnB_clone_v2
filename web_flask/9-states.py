#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask, escape, render_template
from models import storage
from models.base_model import os_type_storage

from models.state import State
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


@app.route('/states_list/', strict_slashes=False)
def states_list():
    ''' displays a list of all State
        objects present in DBStorage sorted by name
        renders an html template
    '''
    states_objs = storage.all('State').values()
    return render_template('7-states_list.html', states=states_objs)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    ''' displays a list of all State
        objects present in DBStorage
        or FileStorage
        sorted by name
        renders an html template
    '''
    if os_type_storage == 'db':
        states_objs = storage.all('State').values()
    else:
        states_objs = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states_objs)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    ''' displays a list of all State
        objects present in DBStorage
        or FileStorage
        sorted by name
        renders an html template
    '''
    if os_type_storage == 'db':
        states_objs = storage.all('State').values()
    else:
        states_objs = storage.all(State).values()
    if id is None:
        return render_template('9-states.html', states=states_objs)
    for state in states_objs:
        if id == state.id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def close_session_db(exit):
    ''' remove the current SQLAlchemy Session '''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
