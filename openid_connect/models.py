from .extensions import db
import datetime


class _TableTemplate:
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Customer(db.Model, _TableTemplate):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

