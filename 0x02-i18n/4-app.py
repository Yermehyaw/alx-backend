#!/usr/bin/env python3
"""
A simple flask app

Modules imported: flask, flask_babel

"""
from flask import (
    Flask,
    render_template,
    request,
)
from flask_babel import (
    Babel,
    _,
)


class Config():
    """Config for Babel obj"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get the locale lang defined from url"""
    locale_arg = request.args.get('locale')
    if locale_arg in app.config['LANGUAGES']:
        return locale_arg
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Homepage"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
