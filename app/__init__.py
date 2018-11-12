from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

# Normal to import after app declaration #
from app.controllers import default