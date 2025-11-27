#!/usr/bin/env python3
"""Flask app with Babel and parametrized templates.

This module sets up a Flask application with Flask-Babel
for internationalization with parametrized templates.
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

    Uses the Accept-Language header from the request to find
    the best matching language from the supported languages.

    Returns:
        str: The best matching language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """Render the index page.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
