"""
Base app
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Default method"""
    return "<p>Hello, World!</p>"
