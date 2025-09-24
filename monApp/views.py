from flask import Flask
from .app import app
from flask import render_template

from config import *
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html",title="R3.01 Dev Web avec Flask", name="Cricri")


@app.route('/about/')
def index1():
    return ABOUT

@app.route('/contact/')
def index2():
    return CONTACT

if __name__== "__main__":
    app.run()