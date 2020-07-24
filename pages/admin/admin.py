from flask import Blueprint, render_template, redirect, url_for, request, flash
from entities import Customer
import re

# Admin Blueprint Definition
admin = Blueprint('admin', __name__, static_folder='static', static_url_path='/admin',
                     template_folder='templates')


#  Routes
@admin.route('/admin')
def index():
    customers_data = Customer().get_all()
    return render_template('admin.html', customers=customers_data)


@admin.route('/add_customer', methods=["POST"])
def add_customer():
    customer = Customer()
    customer.email_address = request.form['email-address']
    customer.user = request.form['user']
    customer.password = request.form['password']
    customer.first_name = request.form['first-name']
    customer.last_name = request.form['last-name']
    customer.country = request.form['country']
    customer.city = request.form['city']
    customer.street = request.form['street']
    customer.number = request.form['number']
    customer.phone_number = request.form['phone-number']
    customer.role = request.form['role']
    is_same_user = customer.get_user_by_user(user=request.form['user-name'])  # true/len>0 if exist
    is_same_mail = customer.get_user_by_email(email_address=request.form['email'])  # true/len>0 if exist
    if not re.match(r"^[A-Za-z0-9\\.\\+_-]+@[A-Za-z0-9\\._-]+\.[a-zA-Z]*$", request.form['email']):
        error = "Email not valid"
        return render_template('sign_up.html', error=error)
    if is_same_user:  # if a user already found, we want to redirect back to sign-up page
        error = "User name already exist"
        return render_template('sign_up.html', error=error)
    if is_same_mail:  # if a email address already found, we want to redirect back to sign-up page
        error = "Email already exist"
        return render_template('sign_up.html', error=error)
    customer.add_customer()
    flash('Added Successfully!')
    return redirect(url_for('admin.index'))


@admin.route('/update_customer', methods=["POST"])
def update_customer():
    Customer().update_customer(request.form['email-address'], request.form['user'], request.form['password'],
                               request.form['first-name'], request.form['last-name'], request.form['country'],
                               request.form['city'], request.form['street'], request.form['number'],
                               request.form['phone-number'], request.form['role'])
    flash('Updated Successfully!')
    return redirect(url_for('admin.index'))


@admin.route('/delete_customer/<string:email_address>', methods=["GET"])
def delete_customer(email_address):
    Customer().delete_customer(email_address)
    flash('Deleted Successfully!')
    return redirect(url_for('admin.index'))

