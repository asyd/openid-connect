from .extensions import db
import datetime
from wtforms_alchemy import ModelForm
# from flask.ext.wtf import FlaskForm
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


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
