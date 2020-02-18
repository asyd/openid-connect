from flask import Blueprint, render_template, jsonify, flash, redirect, url_for, current_app
import flask
from flask_pyoidc.user_session import UserSession
from flask_user import login_required

from .extensions import auth, db, user_manager
from .models import User

bp = Blueprint(
    'ui',
    __name__,
)


@bp.route('/')
@login_required
def hello():
    return render_template('home.html')


# @bp.route('/user/social-login')
@auth.oidc_auth('default')
@user_manager.login_manager.request_loader
def oauth_login(header):
    user_session = UserSession(flask.session, provider_name='default').userinfo
    user = User.query.filter(User.login == user_session['preferred_username'])

    if user.count() == 0:
        user = User(
            login=user_session['preferred_username'],
            firstname=user_session['given_name'],
            lastname=user_session['family_name'],
            email=user_session['email']
        )
        db.session.add(user)
        db.session.commit()
        return user

    return user.first()


@bp.route('/test')
@login_required
def test():
    return render_template('home.html')