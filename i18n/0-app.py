#!/usr/bin/env python3
"""Basic Flask app module.

This module sets up a basic Flask application with a single route
that renders a welcome page.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Render the index page.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
