#!/usr/bin/python3
""" Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


def get_response(route, response):
    @app.route(route, strict_slashes=False)
    def route_func():
        '''return a string given'''
        return response


get_response('/', "Hello HBNB!")
get_response('/hbnb', "HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
