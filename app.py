"""
Base app
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Default method -- hello_world"""
    return "<p>Hello, World!</p>"
