from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from entities import Customer

# sign_up blueprint definition
sign_up = Blueprint('sign_up', __name__, static_folder='static', static_url_path='/sign_up', template_folder='templates')


@sign_up.route('/sign_up', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'GET':
        return render_template('sign_up.html')
    else:
        # signed = Customer(email_adress=request.form['email'],
        #                   user=request.form['user-name'],
        #                   password=request.form['password'],
        #                   first_name=request.form['first-name'],
        #                   last_name=request.form['last-name'],
        #                   country=request.form['country'],
        #                   city=request.form['city'],
        #                   street=request.form['street'],
        #                   number=request.form['number'],
        #                   phone_number=request.form['phone_number'], )
        signed = Customer()
        signed.email_address = request.form['email']
        signed.user = request.form['user-name']
        signed.password = request.form['password']
        signed.first_name = request.form['first-name']
        signed.last_name = request.form['last-name']
        signed.country = request.form['country']
        signed.city = request.form['city']
        signed.street = request.form['street']
        signed.number = request.form['number']
        signed.zip = request.form['zip-code']
        signed.phone_number = request.form.get('phone-number')
        is_same_user = signed.get_user_by_user(user=request.form['user-name'])  # true/len>0 if exist
        is_same_mail = signed.get_user_by_email(email_address=request.form['email'])  # true/len>0 if exist
        if is_same_user:  # if a user already found, we want to redirect back to sign-up page
            error = "User name already exist"
            return render_template('sign_up.html', error=error)
        if is_same_mail:  # if a email address already found, we want to redirect back to sign-up page
            error = "Email already exist"
            return render_template('sign_up.html', error=error)
        if signed:
            session['logged-in']: True
            session['name'] = signed.first_name
            session['email'] = signed.email_address
            session['noOfItems'] = 0  # Not in use
            signed.add_customer()
            flash('You were successfully Signed-up now you can Sign in')

        return redirect(url_for('homepage.index'))

