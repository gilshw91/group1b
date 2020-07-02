from flask import Blueprint, render_template, request, session, flash, redirect, url_for
#from utilities.db.db_manager import dbManager
from entities import *


# customer_page blueprint definition
customer_page = Blueprint('customer_page', __name__, static_folder='static', static_url_path='/customer_page', template_folder='templates')


# Routes
@customer_page.route('/customer_page', methods=['GET', 'POST'])
def index():

        products = Product().get_all()
        reviews = Review().get_reviews(session['email'])
        credit = Credit().get_credit(session['email'])
        histories = Order().get_orders(session['email'])
        address = Customer().get_address(session['email'])
        user_data = Customer().get_user_by_email(session['email'])
        return render_template('customer_page.html', products=products, user_data=user_data, reviews=reviews, credit=credit,
                           histories=histories, address=address)

                           #, reviews=reviews, product_name=product_name)


@customer_page.route('/update_address', methods=['GET', 'POST'])
def update_address():
    city = request.form.get('city')
    street = request.form.get('street')
    number = request.form.get('number')
    zip_code = request.form.get('zip_code')
    Customer().update_address(city, street, number, zip_code, session['email'])

    products = Product().get_all()
    reviews = Review().get_reviews(session['email'])
    credit = Credit().get_credit(session['email'])
    histories = Order().get_orders(session['email'])
    address = Customer().get_address(session['email'])
    user_data = Customer().get_user_by_email(session['email'])

    return redirect(url_for('customer_page.index', products=products, user_data=user_data, reviews=reviews, credit=credit,
                            histories=histories, address=address))


@customer_page.route('/update_password', methods=['POST'])
def update_password():
    old_pass = request.form.get('pwd')
    # new_pass = request.form.get('npwd')
    re_new_pass = request.form.get('npwd2')
    password = dbManager.fetch('SELECT password FROM customer WHERE email_address=%s', (session['email'],))
    if password == old_pass:
        dbManager.commit('UPDATE customer SET password = %s WHERE email_address = %s', (re_new_pass, session['email']))
        flash("Changed successfully")
    else:
        flash("Wrong Password")

    return render_template('customer_page.html')


@customer_page.route('/update_credit', methods=['POST'])
def update_credit():
    credit = request.form.get('credit')
    exp = request.form.get('exp')
    cvv = request.form.get('cvv')
    dbManager.commit('''UPDATE credit SET credit_card_number = %s, expiration_date = %s, cvv = %s
                        WHERE email_address = %s''', (credit, exp, cvv, session['email']))

    return render_template('customer_page.html')
