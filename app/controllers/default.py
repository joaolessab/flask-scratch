# Importing app from app root folder
from app import app, db
from flask import render_template

from app.models.tables import User

# http://127.0.0.1:5000/
@app.route('/')
@app.route('/index')
def index():
    return "Running the API"

# http://127.0.0.1:5000/test/joao
@app.route('/test', defaults = {'name': None})
@app.route('/test/<name>')
def test(name):
    if name:
        return "Hello, %s!" % name
    else:
        return "Hello unknown user!"

# http://127.0.0.1:5000/test/joao
@app.route('/test', methods = ['GET'])
def getExample():
    return "Get request"

@app.route('/html', defaults = {'user': None})
@app.route('/html/<user>')
def html(user):
    return render_template('index.html', user = user)

@app.route('/Mine')
def mine():
    user = User("Joao", "312", "John")
    db.session()
    db.session.commit()