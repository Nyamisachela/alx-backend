#!/usr/bin/env python3
""" Get locale from request
"""
from flask import (
    Flask,
    render_template,
    request
)
from flask_babel imposrt Babel

class Config:
    """config
    """
    LANGUAGES = ['eng', 'fr']
    BABEL_DEFAULT_LOCALE = 'eng'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)

@babel.localselector
def get_locale():
    """determine the best match with supported languages
    """
      return render_template('2-index.html')

  if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=5000)
