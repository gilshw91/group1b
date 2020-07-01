from flask import Blueprint, render_template, redirect, url_for
from entities import *

# homepage blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage', template_folder='templates')


# Routes
@homepage.route('/')
def index():
    products_data = Product().get_all()
    return render_template('homepage.html', products=products_data)


@homepage.route('/homepage')
@homepage.route('/home')
def redirect_homepage():
    return redirect(url_for('homepage.index'))
