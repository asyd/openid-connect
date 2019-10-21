from flask import Blueprint, render_template, jsonify, flash, redirect, url_for
import flask
from flask_pyoidc.user_session import UserSession

from .extensions import auth

bp = Blueprint(
    'ui',
    __name__,
)


@bp.route('/')
def hello():
    return render_template('_base.html')


@bp.route('/login')
@auth.oidc_auth('default')
def login():
    user_session = UserSession(flask.session)
    return jsonify(access_token=user_session.access_token,
                   id_token=user_session.id_token,
                   userinfo=user_session.userinfo)



