"""
Flask Application Entry Point

This module serves as the entry point for the Flask application.

Usage:
    The Flask application is created and initiailized here.
    The prediction blueprint (`api.prediction.bp`) is registered
    with the application.
"""

from flask import Flask

from api.prediction import bp


# flask application instance
app = Flask(__name__)
app.register_blueprint(bp)


if __name__ == '__main__':
    app.run(debug=True)
