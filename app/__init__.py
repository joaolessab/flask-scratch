from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///storage.db'

db = SQLAlchemy(app)

# Normal to import after app declaration #
from app.controllers import default