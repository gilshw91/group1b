from flask import Blueprint, render_template, request
from utilities.db.db_manager import dbManager


# product blueprint definition
product = Blueprint('product', __name__, static_folder='static', static_url_path='/product', template_folder='templates')

product_data = dbManager.fetch('SELECT * FROM product WHERE name=%s', (request.args['name'],))


# Routes
@product.route('/product')
def index():
    if 'name' in request.args:
        product_name = request.args['name']
        product_data = dbManager.fetch('SELECT * FROM product WHERE name=%s', (product_name,))
        if product_data:
            return render_template('product.html', product=product_data[0])
    return render_template('product.html')

# @product.route('{{ product.name }}')
# def index():
#     return render_template('product.html', product=product_data[0])


# @product.route('/extendable_ears')
# def extendable_ears():
#     return render_template('extendable_ears.html')
#
#
# @product.route('/peruvian_instant_darkness_powder')
# def peruvian_instant_darkness_powder():
#     return render_template('peruvian_instant_darkness_powder.html')
#
# def index():
#     product_data = dbManager.fetch('SELECT * FROM product WHERE id=%s', (request.args['id'],))
#     return render_template('product.html', product=product_data[0])