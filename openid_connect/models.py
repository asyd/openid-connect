from .extensions import db
import datetime
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from wtforms import StringField

ModelForm = model_form_factory(FlaskForm)


class _TableTemplate:
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Customer(db.Model, _TableTemplate):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, info={'form_field_class': StringField})


class Project(db.Model, _TableTemplate):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', foreign_keys=[customer_id])


class User(db.Model, _TableTemplate):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Task(db.Model, _TableTemplate):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    label = db.Column(db.String, nullable=False)


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
