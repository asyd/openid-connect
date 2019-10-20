from flask import Flask, url_for, jsonify
from flask_oauthlib.client import OAuth
import os

app = Flask(__name__)
app.secret_key = 'unsecure-key-demo'

app.config['KEYCLOAK'] = {
    'consumer_key': 'flask-demo',
    'consumer_secret': 'ff496a65-7455-4b45-b3ee-39ec31c3166e',
}

oauth = OAuth()
oauth_provider = oauth.remote_app(
    'fask-demo',
    request_token_params={'scope': 'email'},
    base_url='http://asuka.home.opencsi.com:8080/auth/realms/OpenCSI',
    authorize_url='http://asuka.home.opencsi.com:8080/auth/realms/OpenCSI/protocol/openid-connect/auth',
    access_token_url='http://asuka.home.opencsi.com:8080/auth/realms/OpenCSI/protocol/openid-connect/token',
    app_key='KEYCLOAK'
)  # type: OAuthRemoteApp
oauth.init_app(app)


@app.route('/')
def hello():
    return 'Hello world'


@app.route('/login')
def login():
    return oauth_provider.authorize(callback=url_for('authorized', _external=True))


@app.route('/authorized')
def authorized():
    resp = oauth_provider.authorized_response()
    if resp is None:
        return 'Access denied: error=%s'
    return jsonify(resp)


if __name__ == '__main__':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'
    app.run(host='localhost')
