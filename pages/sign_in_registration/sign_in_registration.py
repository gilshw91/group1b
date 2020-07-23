from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from entities import Customer

# Sign_in_registration blueprint definition
sign_in_registration = Blueprint('sign_in_registration', __name__, static_folder='static',
                                 static_url_path='/sign_in_registration', template_folder='templates')


# Routes
@sign_in_registration.route('/sign_in_registration', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'GET':
        return render_template('sign_in_registration.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        user = Customer().get_by_email_password(email, password)
        remember = True if request.form.get('checkbox') else False  # Didnt implement this
        # checks if user exist (len > 0)
        if len(user):
            session['role'] = user[0].role
            session['logged-in'] = True
            session['name'] = user[0].first_name
            session['email'] = email
            session['permanent'] = True
            if session.get('login.errors'):
                del session['login.errors']
                flash('You were successfully logged in')
            return redirect(url_for('homepage.index'))
        else:  # if not registered
            error = 'Please check your login details and try again.'
            session['login.errors'] = 'Login Failed'
    return render_template('sign_in_registration.html', error=error)
