# Importing app from app root folder
from app import app

@app.route('/')
def index():
    return "Running the API"