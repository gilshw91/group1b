from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from entities import *

# sign_up blueprint definition
sign_up = Blueprint('sign_up', __name__, static_folder='static', static_url_path='/sign_up', template_folder='templates')


@sign_up.route('/sign_up', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'GET':
        return render_template('sign_up.html')
    else:
        user = request.form['user-name']
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        country = request.form['country']
        city = request.form['city']
        street = request.form['street']
        number = request.form['number']
        zip = request.form['zip-code']
        phone = request.form['phone-number']  # default, coz not required?
        is_same_user = Customer().get_user_by_user(user)  # true/len>0 if exist
        is_same_mail = Customer().get_user_by_email(email)  # true/len>0 if exist
        if is_same_user:  # if a user already found, we want to redirect back to sign-up page
            error = "User name already exist"
            return render_template('sign_up.html', error=error)
        if is_same_mail:  # if a email address already found, we want to redirect back to sign-up page
            error = "Email already exist"
            return render_template('sign_up.html', error=error)
        signed = Customer().add_customer(email, user, password, first_name, last_name,
                          country, city, street, number, zip, phone)
        if signed:
            session['logged-in']: True
            session['name'] = first_name
            session['email'] = email
            session['noOfItems'] = 0
            flash('You were successfully Signed-up now you can Sign in')
        return redirect(url_for('homepage.index'))

