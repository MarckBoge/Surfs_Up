from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/product/<name>')
def get_product(name):
    return "The product is " + str(name)
    