#!/usr/bin/python3
""" Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)

def create_route(route, response):
    @app.route(route, strict_slashes=False)
    def route_function():
        """Return a given string"""
        return response

create_route('/', "Hello HBNB!")
create_route('/hbnb', "HBNB")
create_route('/c/<text>', "C {}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
