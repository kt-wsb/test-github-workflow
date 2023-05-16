"""
This is a Flask application that greets WSB.
"""

from flask import Flask

app = Flask(_name_)

@app.route('/')
def index():
    """
    Handler for the root URL.
    """
    return '<h1>Hello WSB! Greetings from Flask!</h1>'

if _name_ == "_main_":
    app.run(debug=True)
