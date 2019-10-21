from flask import Blueprint, render_template, flash
from .models import CustomerForm, Customer
from .extensions import db

bp = Blueprint(
    'admin',
    __name__,
    url_prefix='/admin'
)


@bp.route('/customers', methods=['GET', 'POST'])
def customers():
    flash("Hello world")
    form = CustomerForm()
    if form.validate_on_submit():
        customer = Customer()
        form.populate_obj(customer)
        db.session.add(customer)
        db.session.commit()

    customers = Customer.query.all()
    return render_template('customers.html',
                           customers=customers,
                           form=form)



