from flask import Blueprint, render_template, request, session, redirect, url_for
from entities import *


# customer_page blueprint definition
customer_page = Blueprint('customer_page', __name__, static_folder='static', static_url_path='/customer_page', template_folder='templates')


# Routes
@customer_page.route('/customer_page', methods=['GET', 'POST'])
def index():
    email = session['email']
    products = Product().get_all()
    reviews = Review().get_review_by_email(email)
    credit = Credit().get_credit_by_email(email)
    histories = Order().get_history(email)
    address = Customer().get_address(email)
    user_data = Customer().get_user_by_email(email)
    return render_template('customer_page.html', products=products, user_data=user_data, reviews=reviews, credit=credit,
                           histories=histories, address=address)

@customer_page.route('/update_address', methods=['GET', 'POST'])
def update_address():
    email = session['email']
    country = request.form['country']
    city = request.form['city']
    street = request.form['street']
    number = request.form['number']
    zip_code = request.form['zip_code']
    # Updates with address
    Customer().update_address(country, city, street, number, zip_code, email)
    products = Product().get_all()
    reviews = Review().get_review_by_email(email)
    credit = Credit().get_credit_by_email(email)
    histories = Order().get_history(email)
    address = Customer().get_address(email)
    user_data = Customer().get_user_by_email(email)
    return redirect(url_for('customer_page.index', products=products, user_data=user_data, reviews=reviews, credit=credit,
                            histories=histories, address=address))


@customer_page.route('/update_password', methods=['POST'])
def update_password():
    email = session['email']
    old_pass = request.form.get('pwd')
    # new_pass = request.form.get('npwd')
    re_new_pass = request.form.get('npwd2')
    password = Customer().get_password(email)
    if password == old_pass:
        Customer().change_password(re_new_pass, email)
        # flash("Changed successfully")
    else:
        flash("Wrong Password")
    return render_template('customer_page.html')


@customer_page.route('/update_credit', methods=['POST'])
def update_credit():
    email = session['email']
    credit = request.form.get('credit')
    exp = request.form.get('exp')
    cvv = request.form.get('cvv')
    has_credit = Credit().get_credit_by_email(email)
    if has_credit:
        Credit().update_credit(credit, exp, cvv, email)

    return redirect(url_for('customer_page.index'))
