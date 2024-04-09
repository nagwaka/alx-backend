#!/usr/bin/evn python3
"""
Basic Babel setup
"""
from flask import Flask
from flask_babel import Babel


class Config:
    """
    Configs available languages for the Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    
    
app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)
