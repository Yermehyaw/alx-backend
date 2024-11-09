#!/usr/bin/env python3
"""
A simple flask app

Modules imported: flask

"""
from flask import (
    Flask,
    render_template,
)
from flask_babel import Babel


class Config():
    """Config for Babel obj"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Homepage"""
    return render_template('0-index.html')
