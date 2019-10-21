from flask_sqlalchemy import SQLAlchemy
from flask_pyoidc import OIDCAuthentication

db = SQLAlchemy()

auth = OIDCAuthentication(None)
