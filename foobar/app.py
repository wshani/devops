import sys, os, logging

from .foo import foo
from .bar import bar
from flask import Flask

logger = logging.getLogger('foobar')
hdlr   = logging.FileHandler('/data/foobar.log')
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route("/")
def main():
    logger.debug('Got main') 
    return "Foobar!"

@app.route("/foo")
def get_foo():
    logger.debug('Got foo')
    return foo()

@app.route("/bar")
def get_bar():
    logger.debug('Got bar')
    return bar()

