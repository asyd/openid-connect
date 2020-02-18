import socket
import datetime

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/dev.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'unsecure-dev-key'
SERVER_NAME = 'asuka.home.opencsi.com:5000'

PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=7).total_seconds()
PREFERRED_URL_SCHEME = "http"

OIDC_PROVIDER = {
    'client_id': 'flask-demo',
    'client_secret': 'ff496a65-7455-4b45-b3ee-39ec31c3166e',
    'issuer': 'http://asuka.home.opencsi.com:8080/auth/realms/OpenCSI',
}

USER_APP_NAME = 'OpenCSI TimeTracking'
USER_ENABLE_EMAIL = False
USER_ENABLE_USERNAME = False
USER_EMAIL_SENDER_NAME = USER_APP_NAME
USER_EMAIL_SENDER_EMAIL = 'noreply@opencsi.com'
