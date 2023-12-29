#!/usr/bin/python3
"""
script using Flask to create a web application with the specified routes
"""
from flask import Flask, render_template


app = Flask(__name__)


# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


# Route to display "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# Route to display "C ", followed by the value of the text variable
@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    processed_text = text.replace('_', ' ')
    return f'C {processed_text}'


# Route to display "Python ", followed by the value of the text variable
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is_cool"):
    processed_text = text.replace('_', ' ')
    return f'Python {processed_text}'


# Route to display "n is a number" only if n is an integer
@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return f'{n} is a number'


# Route to display a HTML page if n is an integer and show if it's odd or even
@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    else:
        return 'Not an integer!'


# Route to display a HTML page indicating if n is even or odd
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    if isinstance(n, int):
        parity = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', n=n, parity=parity)
    else:
        return 'Not an integer!'


if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
