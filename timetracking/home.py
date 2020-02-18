from flask import Blueprint, render_template, jsonify, flash, redirect, url_for, current_app
import flask
from flask_pyoidc.user_session import UserSession
from flask_user import login_required
from flask_login import login_user

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


@bp.route('/user/social-login')
@auth.oidc_auth('default')
# @user_manager.login_manager.request_loader
def oauth_login():
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
        flask_user, _ = user_manager.db_manager.get_user_and_user_email_by_email(user_session['email'])
        print(user_session['email'])
        return user

    print(user.first().email)
    # TODO: logged user and redirect to home page
    flask_user, _ = user_manager.db_manager.get_user_and_user_email_by_email(user.first().email)
    login_user(flask_user)
    return redirect('/')
    # return user.first()


@bp.route('/test')
@login_required
def test():
    return render_template('home.html')
