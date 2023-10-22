#!/usr/bin/python3
""" Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)

def route_with_response(route, response=None):
    def decorator(func):
        @app.route(route, strict_slashes=False)
        def wrapper(*args, **kwargs):
            text = response if response is not None else kwargs.get('text', '')
            return func(text)

        return wrapper

    return decorator

@route_with_response('/')
def hello(text="Hello HBNB!"):
    return text

@route_with_response('/hbnb', "HBNB")
def hbnb(text):
    return text

@route_with_response('/c/<text>', "C {text}")
def cText(text):
    return text

@route_with_response('/python')
@route_with_response('/python/<text>', "Python {text}")
def pythonText(text):
    return text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
