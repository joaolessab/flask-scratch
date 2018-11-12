# Importing app from app root folder
from app import app

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