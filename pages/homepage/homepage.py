from flask import Blueprint, render_template, redirect, url_for, request
from utilities.db.db_manager import dbManager
# homepage blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage', template_folder='templates')


# Routes
@homepage.route('/')
def index():
    products_data = dbManager.fetch('SELECT * FROM product')

    return render_template('homepage.html', products=products_data)


@homepage.route('/homepage')
@homepage.route('/home')
def redirect_homepage():
    return redirect(url_for('homepage.index'))
