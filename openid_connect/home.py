from flask import Flask, url_for, jsonify
import flask
from flask_pyoidc import OIDCAuthentication
from flask_pyoidc.provider_configuration import ProviderConfiguration, ClientMetadata
from flask_pyoidc.user_session import UserSession
import datetime

app = Flask(__name__)
app.config.update({'SERVER_NAME': 'asuka.home.opencsi.com:5000',
                   'SECRET_KEY': 'dev_key',  # make sure to change this!!
                   'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=7).total_seconds(),
                   'PREFERRED_URL_SCHEME': 'http',
                   'DEBUG': True})

keycloak = ClientMetadata(
    client_id='flask-demo',
    client_secret='ff496a65-7455-4b45-b3ee-39ec31c3166e'
)
config = ProviderConfiguration(
    issuer='http://asuka.home.opencsi.com:8080/auth/realms/OpenCSI',
    client_metadata=keycloak
)
auth = OIDCAuthentication({'default': config}, app)


@app.route('/')
def hello():
    return 'Hello world'


@app.route('/login')
@auth.oidc_auth('default')
def login():
    user_session = UserSession(flask.session)
    return jsonify(access_token=user_session.access_token,
                   id_token=user_session.id_token,
                   userinfo=user_session.userinfo)


if __name__ == '__main__':
    app.run(host='asuka.home.opencsi.com', port=5000)
