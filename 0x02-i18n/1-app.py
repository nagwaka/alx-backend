#!/usr/bin/evn python3
"""
Basic Babel setup
"""
from flask import Flask, render_template
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


@app.route('/')
def get_index() -> str:
    """
    Outputs a message
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
