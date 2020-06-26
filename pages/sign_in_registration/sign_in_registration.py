from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from utilities.db.db_manager import dbManager

# sign_in_registration blueprint definition
sign_in_registration = Blueprint('sign_in_registration', __name__, static_folder='static',
                                 static_url_path='/sign_in_registration', template_folder='templates')


# Routes
@sign_in_registration.route('/sign_in_registration', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('sign_in_registration.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        user = dbManager.fetch('SELECT * FROM customer WHERE email_address=%s AND password=%s', (email, password))
        remember = True if request.form.get('checkbox') else False
        # checks if user exist (len > 0)
        if len(user):
            session['logged-in'] = True
            session['name'] = user[0].first_name
            session['email'] = email
            if session.get('login.errors'):
                del session['login.errors']
            return redirect(url_for('homepage.index'))
        else:  # if not registered
            # # user = dbManager.commit('INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            # #                         (email_address, user, password, first_name, last_name, country, city,
            # #                          street, number, phone_number)
            #
            flash('Please check your login details and try again.')
            session['login.errors'] = 'Login Failed'
    return redirect(url_for('sign_in_registration.index'))


# @sign_in_registration.route('/sign_in_registration')
# def sign_out():
#     if session.get('logged-in'):  # if the user clicked sign out, clear and go to homepage
#         # session['logged-in'] = False
#         session.clear()
#         return render_template(url_for('homepage.index'))