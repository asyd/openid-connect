import socket
import datetime

SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
SECRET_KEY = 'unsecure-dev-key'
SERVER_NAME = 'asuka.home.opencsi.com:5000'

PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=7).total_seconds()
PREFERRED_URL_SCHEME = "http"

OIDC_PROVIDER = {
    'client_id': 'flask-demo',
    'client_secret': 'ff496a65-7455-4b45-b3ee-39ec31c3166e',
    'issuer': 'http://asuka.home.opencsi.com:8080/auth/realms/OpenCSI',
}
