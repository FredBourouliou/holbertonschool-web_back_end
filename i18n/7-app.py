#!/usr/bin/env python3
"""Flask app with timezone selection.

This module sets up a Flask application with Flask-Babel
that supports timezone selection with priority ordering.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict
import pytz


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

    Priority order:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale

    Returns:
        str: The best matching language code.
    """
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # 2. Locale from user settings
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    # 3. Locale from request header
    header_locale = request.accept_languages.best_match(
        app.config['LANGUAGES'])
    if header_locale:
        return header_locale

    # 4. Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


def get_timezone() -> str:
    """Determine the appropriate timezone.

    Priority order:
    1. Timezone from URL parameters
    2. Timezone from user settings
    3. Default to UTC

    Returns:
        str: The appropriate timezone string.
    """
    # 1. Timezone from URL parameters
    tz_param = request.args.get('timezone')
    if tz_param:
        try:
            pytz.timezone(tz_param)
            return tz_param
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # 2. Timezone from user settings
    if g.user:
        user_tz = g.user.get('timezone')
        if user_tz:
            try:
                pytz.timezone(user_tz)
                return user_tz
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    # 3. Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/')
def index() -> str:
    """Render the index page.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
