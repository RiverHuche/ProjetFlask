from flask import Flask, config
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"


@app.route('/about/')
def index1():
    return config.ABOUT
if __name__== "__main__":
    app.run()