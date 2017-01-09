import sys, os

from .foo import foo
from .bar import bar
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Foobar!"

@app.route("/foo")
def get_foo():
    return foo()

@app.route("/bar")
def get_bar():
    return bar()

