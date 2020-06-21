from flask import Blueprint, render_template, request
from utilities.db.db_manager import dbManager



# product blueprint definition
product = Blueprint('product', __name__, static_folder='static', static_url_path='/product', template_folder='templates')


# Routes
@product.route('/product')
def index():
    product_data = dbManager.fetch('SELECT * FROM product WHERE id=%s', (request.args['id'],))
    return render_template('product.html', product=product_data[0])


