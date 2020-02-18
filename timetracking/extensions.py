from flask_sqlalchemy import SQLAlchemy
from flask_pyoidc import OIDCAuthentication
from flask_user import UserManager

db = SQLAlchemy()

auth = OIDCAuthentication(None)

user_manager = UserManager(None, None, None)