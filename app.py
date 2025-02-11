from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    Hello world
    This is a simple flash app for demo purpose
    """