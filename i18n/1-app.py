#!/usr/bin/env python3
"""Basic Flask app with Babel setup.

This module sets up a Flask application with Flask-Babel
for internationalization support.
"""
from flask import Flask, render_template
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
babel = Babel(app)


@app.route('/')
def index() -> str:
    """Render the index page.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
