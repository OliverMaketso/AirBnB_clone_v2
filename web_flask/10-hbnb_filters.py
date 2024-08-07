#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


# Declare a method to handle @app.teardown_appcontext
@app.teardown_appcontext
def teardown(exception):
    """Closes the SQLAlchemy Session.(Handle teardown)"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    /states folder with an id

    Returns:
        [HTML content: [display a HTML page: (inside the tag BODY)]
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)