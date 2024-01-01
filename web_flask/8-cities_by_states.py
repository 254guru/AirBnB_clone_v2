#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    cities_and_states = []
    for state in states:
        cities = []
        if type(storage).__name__ == 'DBStorage':
            cities = state.cities
        else:
            cities = state.cities()
        cities = sorted(cities, key=lambda city: city.name)
        cities_and_states.append((state, cities))
    return render_template('8-cities_by_states.html',
                           states=states, cities_and_states=cities_and_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
