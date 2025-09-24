from .app import app
from flask import render_template
from config import *

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html",title="R3.01 Dev Web avec Flask", name="Cricri")


@app.route('/about/')
def about():
    return ABOUT

@app.route('/contact/')
def contact():
    return CONTACT

if __name__== "__main__":
    app.run()