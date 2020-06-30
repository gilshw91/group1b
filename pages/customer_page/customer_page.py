from flask import Blueprint, render_template, request, session, flash
from utilities.db.db_manager import dbManager


# customer_page blueprint definition
customer_page = Blueprint('customer_page', __name__, static_folder='static', static_url_path='/customer_page', template_folder='templates')


# Routes
@customer_page.route('/customer_page')
def index():
    products = dbManager.fetch('SELECT * FROM product')
    # reviews = dbManager.fetch('SELECT * FROM review WHERE email_address = %s', (session['email'],))
    # product_name = dbManager.fetch('''
    # SELECT name from product
    # WHERE product.id = %s''', (reviews.id,))
    user_data = dbManager.fetch('SELECT * FROM customer')
    return render_template('customer_page.html', products=products, user_data=user_data)
                           #, reviews=reviews, product_name=product_name)


@customer_page.route('/update_address', methods=['POST'])
def update_address():
    city = request.form.get('city')
    street = request.form.get('street')
    number = request.form.get('number')
    zip_code = request.form.get('zip_code')
    dbManager.commit('UPDATE customer SET city = %s, street = %s, number = %s', (city, street, number))
    dbManager.commit('UPDATE zips SET zip = %s', (zip_code,))

    return render_template('customer_page.html')


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
