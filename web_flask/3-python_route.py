#!/usr/bin/python3
"""This route module
starts a Flask web application.
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Prints  hello message"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def show_hbnb():
    """Prints  hbnb message"""
    return 'HBNB'


@app.route('/c/<text>')
def disp_c(text):
    """Prints  c with text message"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """return Python, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
