from flask import Blueprint, render_template, flash, redirect, url_for, request
from .models import CustomerForm, Customer, Project, ProjectForm, Task, TaskForm, User
from .extensions import db

bp = Blueprint(
    'admin',
    __name__,
    url_prefix='/admin'
)


@bp.route('/customers', methods=['GET', 'POST'])
def customers():
    return render_template('customers.html',
                           customers=Customer.query.all(),
                           form=CustomerForm())


@bp.route('/customers/<customer_id>')
def customer(customer_id: int):
    form = ProjectForm()
    current_customer = Customer.query.filter(Customer.id == customer_id).first()
    projects = Project.query.filter(Project.customer_id == customer_id).all()

    return render_template('customer_detail.html',
                           projects=projects,
                           current_customer=current_customer,
                           form=form
                           )


@bp.route('/customer/new', methods=['POST'])
def customer_new():
    form = CustomerForm()
    if form.validate_on_submit():
        new_customer = Customer()
        form.populate_obj(new_customer)
        db.session.add(new_customer)
        db.session.commit()
        flash("Customer added")

    return redirect(url_for('admin.customers'))


@bp.route('/project/<int:project_id>')
def project_detail(project_id: int):
    form = TaskForm()
    form.user_id.choices = [(x.id, x.login) for x in User.query.all()]
    if form.validate_on_submit():
        pass
    else:
        tasks = Task.query.filter(Task.project_id == project_id)
        return render_template('project_details.html',
                               form=form,
                               current_project=Project.query.filter(Project.id == project_id).one(),
                               tasks=tasks)


@bp.route('/project/new', methods=['POST'])
def project_new():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project()
        form.populate_obj(project)
        db.session.add(project)
        db.session.commit()
        flash("Project added")

    return redirect(url_for('admin.customer',
                            customer_id=project.customer_id))


@bp.route('/task/new', methods=['POST'])
def task_new():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task()
        form.populate_obj(task)
        db.session.add(task)
        db.session.commit()
        flash("Task added")

    return redirect(url_for('admin.project', project_id=task.project_id))
