#!/usr/bin/python3
"""
script that creates a Flask web application with the specified routes
"""
from flask import Flask, escape


app = Flask(__name__)


# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


# Route to display "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# Route to display "C " followed by the value of the text variable
@app.route('/c/<text>', strict_slashes=False)
@app.route('/c/', strict_slashes=False)
def display_c(text='is_cool'):
    processed_text = escape(text).replace('_', ' ')
    return f'C {processed_text}'


# Route to display "Python " followed by the value of the text variable
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python(text='is_cool'):
    processed_text = escape(text).replace('_', ' ')
    return f'Python {processed_text}'


if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
