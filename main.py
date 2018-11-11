from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return "Running the API"

# Security to verify if the main file is being called #
if __name__ == "__main__":
    app.run()