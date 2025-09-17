from flask import Flask

from config import *
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"


@app.route('/about/')
def index1():
    return ABOUT

@app.route('/contact/')
def index2():
    return CONTACT

if __name__== "__main__":
    app.run()