from timetracking.app import create_app
import os

environment = 'development'

try:
    environment = os.environ['FLASK_ENV']
except KeyError:
    pass

app = create_app(environment)
