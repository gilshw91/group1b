from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from utilities.db.db_manager import dbManager

# sign_up blueprint definition
sign_up = Blueprint('sign_up', __name__, static_folder='static', static_url_path='/sign_up', template_folder='templates')


@sign_up.route('/sign_up', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('sign_up.html')
    else:
        new_user = request.form.get('user-name')
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        country = request.form.get('country')
        city = request.form.get('city')
        street = request.form.get('street')
        number = request.form.get('number')
        # zip = request.form.get('zip-code')
        country = request.form.get('country')
        phone = request.form.get('phone-number') # default, coz not required?
        customer = dbManager.fetch('SELECT * FROM customer WHERE customer.user=%s', (new_user,))
        if new_user == customer:  # if a user already found, we want to redirect back to signup page
            flash("User name already exist")
            return redirect(url_for('sign_up.index'))
        dbManager.commit("INSERT INTO customer('email_address', 'user', 'password', 'first_name','last_name', \
                         'country', 'city', 'street', 'number', 'phone_number') VALUES(%s, %s, \
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (new_user, email, password, first_name, last_name,
                         country, city, street, number, phone))
        session['logged-in']: True
        session['name'] = first_name
        session['email'] = email
        return redirect(url_for('homepage.index'))

