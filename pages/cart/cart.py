from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from utilities.db.db_manager import dbManager

# cart blueprint definition
cart = Blueprint('cart', __name__, static_folder='static', static_url_path='/cart', template_folder='templates')


@cart.route("/cart")
def index():
    if not session.get('email'):
        return redirect(url_for('sign_in_registration.index'))
    user_mail = session['email']
    user_items = dbManager.fetch('''
        SELECT product.id, product.name, product.price, product.img 
        FROM product 
        JOIN cart
        WHERE product.id = cart.product_id 
        AND cart.email_address = %s''', (user_mail,))

    items = dbManager.fetch("SELECT * FROM cart WHERE email_address = %s", (user_mail,))
    noOfItems = 0
    for item in items:
        noOfItems += 1

    total_price = 0
    for row in user_items:
        total_price += row[2]
    return render_template("cart.html", products=user_items, totalPrice=total_price, loggedIn=session['logged-in'],
                           firstName=session['name'], noOfItems=noOfItems)

