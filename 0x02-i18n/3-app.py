#!/usr/bin/env python3
"""
A simple flask app

Modules imported: flask

"""
from flask import (
    Flask,
    render_template,
    request,
    Response,
)
from flask_babel import (
    Babel,
    _,
)


class Config():
    """Config for Babel obj

    Attrributes:
    LANGUAGES: supported languages
    DEFAULT: default lang and tinezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get the locale lang defined from url"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Homepage"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
