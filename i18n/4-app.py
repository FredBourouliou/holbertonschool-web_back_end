#!/usr/bin/env python3
"""Flask app with URL parameter locale selection.

This module sets up a Flask application with Flask-Babel
that supports forcing locale via URL parameter.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


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
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
