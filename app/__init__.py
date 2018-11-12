from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

# Migrate takes care of my migrations #
# Manager takes care of my commands #
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Normal to import after app declaration #
from app.controllers import default