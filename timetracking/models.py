from .extensions import db
import datetime
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory, ModelFieldList
from wtforms import StringField, IntegerField, FieldList, FormField, SelectField
from flask_user import UserMixin

BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(cls):
        return db.session


class _TableTemplate:
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Customer(db.Model, _TableTemplate):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, info={'form_field_class': StringField}, unique=True)


class Project(db.Model, _TableTemplate):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', foreign_keys=[customer_id])


class User(db.Model, _TableTemplate, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"{self.firstname.title()} {self.lastname.title()}"


class Role(db.Model, _TableTemplate):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)


class Task(db.Model, _TableTemplate):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    adr = db.Column(db.Integer, nullable=False, default=0)
    amount = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', foreign_keys=[user_id])
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', foreign_keys=[project_id])


class ProjectForm(ModelForm):
    class Meta:
        model = Project

    customer_id = IntegerField()


class CustomerForm(ModelForm):
    class Meta:
        model = Customer


class UserForm(ModelForm):
    class Meta:
        model = User


class TaskForm(ModelForm):
    class Meta:
        model = Task

    project_id = IntegerField()
    user_id = SelectField('User', coerce=int)
    # user =
    # user = FieldList(StringField('user_login'))
