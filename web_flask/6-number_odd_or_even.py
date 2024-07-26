#!/usr/bin/python3
"""This module starts a web app"""
from flask import Flask, render_template

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
    text = text.replace('_',' ')
    return "C %s" % text

@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """returns python followed by the value of text variable"""
    text = text.replace('_',' ')
    return "python %s" % text

@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """returns n  which is an integer"""
    return "{} is a number". format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """returns n  which is an integer"""
    return render_template("5-number.html", num=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_number_even(n):
    """returns n  which is an integer"""
    even_or_odd = 'even' if n % 2 == 0 else 'odd'
    return render_template("6-number_odd_or_even.html", num=n, ans=even_or_odd)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)