#!/usr/bin/env python3
"""Flask app with mock user login.

This module sets up a Flask application with Flask-Babel
that supports mock user login via URL parameter.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


class Config:
    """Configuration class for Flask app.

    This class contains configuration settings for the Flask application,
    including available languages and default locale/timezone settings.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Get user from mock database.

    Retrieves a user dictionary based on the login_as URL parameter.

    Returns:
        dict or None: User dictionary if found, None otherwise.
    """
    login_as = request.args.get('login_as')
    if login_as:
        try:
            user_id = int(login_as)
            return users.get(user_id)
        except ValueError:
            return None
    return None


@app.before_request
def before_request() -> None:
    """Execute before all other functions.

    Finds a user if any and sets it as a global on flask.g.user.
    """
    g.user = get_user()


def get_locale() -> str:
    """Determine the best match for supported languages.

    First checks if a locale parameter is present in the URL and if it's
    a supported locale. If not, uses the Accept-Language header from the
    request to find the best matching language.

    Returns:
        str: The best matching language code.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """Render the index page.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
