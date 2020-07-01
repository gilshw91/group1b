from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from utilities.db.db_manager import dbManager


# customer_page blueprint definition
customer_page = Blueprint('customer_page', __name__, static_folder='static', static_url_path='/customer_page', template_folder='templates')


# Routes
@customer_page.route('/customer_page')
def index():
    products = dbManager.fetch('SELECT * FROM product')
    reviews = dbManager.fetch('''SELECT r.date, r.rank, r.content, r.email_address, p.name
                                FROM review AS r 
                                JOIN product AS p ON r.id=p.id 
                                WHERE email_address=%s''', (session['email'],))
    credit = dbManager.fetch('SELECT * FROM credit WHERE email_address=%s', (session['email'],))
    histories = dbManager.fetch('''SELECT o.number, o.date_of_order, o.email_address, i.quantity, p.id,
                                            p.name, p.price, p.img
                                FROM `order` AS o 
                                JOIN include AS i ON o.number=i.number 
                                JOIN product AS p ON i.sku=p.id
                                WHERE email_address=%s''', (session['email'],))
    address = dbManager.fetch('''SELECT c.email_address, c.country, c.city, c.street, c.number, z.zip 
                                FROM customer AS c 
                                JOIN zips AS z ON c.country=z.country 
                                AND c.city=z.city AND c.street=z.street AND c.number=z.number 
                                WHERE email_address=%s''', (session['email'],))
    # product_name = dbManager.fetch('''
    # SELECT name from product
    # WHERE product.id = %s''', (reviews.id,))
    user_data = dbManager.fetch('SELECT * FROM customer WHERE email_address = %s', (session['email'],))
    return render_template('customer_page.html', products=products, user_data=user_data, reviews=reviews, credit=credit,
                           histories=histories, address=address)

                           #, reviews=reviews, product_name=product_name)


@customer_page.route('/update_address', methods=['POST'])
def update_address():
    city = request.form.get('city')
    street = request.form.get('street')
    number = request.form.get('number')
    zip_code = request.form.get('zip_code')
    dbManager.commit('UPDATE customer SET city = %s, street = %s, number = %s', (city, street, number))
    dbManager.commit('UPDATE zips SET zip = %s', (zip_code,))

    products = dbManager.fetch('SELECT * FROM product')
    reviews = dbManager.fetch('''SELECT r.date, r.rank, r.content, r.email_address, p.name
                                    FROM review AS r 
                                    JOIN product AS p ON r.id=p.id 
                                    WHERE email_address=%s''', (session['email'],))
    credit = dbManager.fetch('SELECT * FROM credit WHERE email_address=%s', (session['email'],))
    histories = dbManager.fetch('''SELECT o.number, o.date_of_order, o.email_address, i.quantity, p.id,
                                                p.name, p.price, p.img
                                    FROM `order` AS o 
                                    JOIN include AS i ON o.number=i.number 
                                    JOIN product AS p ON i.sku=p.id
                                    WHERE email_address=%s''', (session['email'],))
    address = dbManager.fetch('''SELECT c.email_address, c.country, c.city, c.street, c.number, z.zip 
                                    FROM customer AS c 
                                    JOIN zips AS z ON c.country=z.country 
                                    AND c.city=z.city AND c.street=z.street AND c.number=z.number 
                                    WHERE email_address=%s''', (session['email'],))
    # product_name = dbManager.fetch('''
    # SELECT name from product
    # WHERE product.id = %s''', (reviews.id,))
    user_data = dbManager.fetch('SELECT * FROM customer WHERE email_address = %s', (session['email'],))

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
