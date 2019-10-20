from flask import Flask, url_for, jsonify
import os
from flask_pyoidc import OIDCAuthentication
from flask_pyoidc.provider_configuration import ProviderConfiguration, ClientRegistrationInfo
from flask_pyoidc.user_session import UserSession

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost'
app.secret_key = 'unsecure-key-demo'

keycloak = ClientRegistrationInfo(
    client_id='flask-demo',
    client_secret='ff496a65-7455-4b45-b3ee-39ec31c3166e'
)
config = ProviderConfiguration(
    issuer='http://asuka.home.opencsi.com:8080/auth/realms/OpenCSI',
    client_registration_info=keycloak
)
auth = OIDCAuthentication({'default': config}, app)


@app.route('/')
def hello():
    return 'Hello world'


@app.route('/login')
@auth.oidc_auth('default')
def login():
    return 'hello world'


if __name__ == '__main__':
    app.run(host='asuka.home.opencsi.com', port=5000)
