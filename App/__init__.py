"""App package initializer."""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (insta485/config.py)
app.config.from_object('App.config')

# Overlay settings read from a Python file whose path is set in the environment
# variable INSTA485_SETTINGS. Setting this environment variable is optional.
# Docs: http://flask.pocoo.org/docs/latest/config/
#
# EXAMPLE:
# $ export APP_SETTINGS=secret_key_config.py
app.config.from_envvar('APP_SETTINGS', silent=True)

# Tell our App about views and model.  This is dangerously close to a
# circular import, but Flask was designed that way.
# (Reference http://flask.pocoo.org/docs/patterns/packages/)
import App.views
import App.model  
