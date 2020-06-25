from flask import Blueprint, render_template, request, redirect, url_for, session
from utilities.db.db_manager import dbManager


# sign_in_registration blueprint definition
sign_in_registration = Blueprint('sign_in_registration', __name__, static_folder='static', static_url_path='/sign_in_registration', template_folder='templates')


# Routes
@sign_in_registration.route('/sign_in_registration', methods=['GET', 'POST'])
def index():
    if session.get('logged_in'):  # if the user clicked sign out, clear and go to homepage
        session.clear()
        return redirect(url_for('homepage.index'))
    if request.method == 'GET':
        return render_template('sign_in_registration.html')
    else:
        email = request.form.get('email_address')  # as the name in the form, every get is from type string
        password = request.form.get('password')
        user = dbManager.fetch('SELECT * FROM customer WHERE email=%s AND password=%s', (email, password))
        # checks if user exist (len > 0)
        if len(user):
            session['login'] = {
                'logged-in': True,
                'name': user[0].first_name
            }
            del session['login.errors']
            return redirect(url_for('homepage.index'))
        else:  # if not registered
            # # user = dbManager.commit('INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            # #                         (email_address, user, password, first_name, last_name, country, city,
            # #                          street, number, phone_number)
            #                         )
            return redirect(url_for('homepage.index'))
    session['login.errors'] = 'Login Failed'
    return redirect(url_for('sign_in_registration.index'))
