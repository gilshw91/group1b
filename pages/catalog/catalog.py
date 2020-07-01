from flask import Blueprint, render_template, request
from utilities.db.db_manager import dbManager
from entities import Product

# catalog blueprint definition
catalog = Blueprint('catalog', __name__, static_folder='static', static_url_path='/catalog', template_folder='templates')


# Routes
@catalog.route('/catalog')
def index():
    products_data = Product().get_products()
    return render_template('catalog.html', products=products_data)

