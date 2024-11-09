#!/usr/bin/env python3
"""
A simple flask app

Modules imported: flask

"""
from flask import (
    Flask,
    render_template,
)


app = Flask(__name__)


@app.route('/')
def index():
    """Homepage"""
    return render_template('0-index.html')
