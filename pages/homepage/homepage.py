from flask import Blueprint, render_template, redirect, url_for
from entities import *

# Homepage Blueprint Definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage',
                     template_folder='templates')


#  Routes
@homepage.route('/')
def index():
    products_data = Product().get_all()  # The products that will appear in the carousel
    product_week = Product().get_product(100000002)  # The product that will be pop-up as the product of the week
    return render_template('homepage.html', products=products_data, product_week=product_week)


@homepage.route('/homepage')
@homepage.route('/home')
def redirect_homepage():
    return redirect(url_for('homepage.index'))
