#!/usr/bin/env python3
"""
A simple flask app

Modules imported: flask, flask_babel, typing

"""
from flask import (
    Flask,
    render_template,
    request,
    Response,
    g,
)
from flask_babel import (
    Babel,
    _,
)
from typing import (
    Dict,
    Union
)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """Config for Babel obj"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get the locale lang defined from url"""
    # url param for locale takes first priority
    locale_arg = request.args.get('locale')
    if locale_arg in app.config['LANGUAGES']:
        return locale_arg

    # followed by user settings
    locale = g.user['locale']
    if locale:
        return locale

    # then frm the request header
    locale = request.headers.get('Accept-Language')
    if locale:
        return locale

    #  default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.before_request
def before_request() -> None:
    """Sets the user to the g global"""
    # find user
    user_info = get_user()

    if user_info:
        g.user = user_info


@app.route('/')
def index() -> Response:
    """Homepage"""
    return render_template('6-index.html')


def get_user() -> Union[Dict, None]:
    """Gets the info on a user by user id"""
    user_id = request.args.get('login_as')

    if user_id:
        try:
            user_id = int(user_id)
        except ValueError:
            return

        return users.get(user_id)


if __name__ == '__main__':
    app.run(debug=True)
