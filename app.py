"""
This is a Flask application that greets WSB.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """
    Handler for the root URL.
    """
    return '<h1>Hello WSB! Greetings from Flask!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
