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

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
