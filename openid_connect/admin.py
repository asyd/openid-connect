from flask import Blueprint, render_template, jsonify, flash, redirect, url_for
import flask
from flask_pyoidc.user_session import UserSession

from .extensions import auth

bp = Blueprint(
    'admin',
    __name__,
    url_prefix='/admin'
)


@bp.route('/customers')
def hello():
    return render_template('_base.html')





