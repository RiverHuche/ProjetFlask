from flask import Flask

from config import *
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"


@app.route('/about/')
def index1():
    return ABOUT

if __name__== "__main__":
    app.run()