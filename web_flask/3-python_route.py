#!/usr/bin/python3
"""This module starts a web app"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """returns c followed by the value of text variable"""
    text = text.replace('_', ' ')
    return "C %s" % text


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """returns c followed by the value of text variable"""
    text = text.replace('_', ' ')
    return "Python %s" % text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
