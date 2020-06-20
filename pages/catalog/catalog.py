from flask import Blueprint, render_template, request
from utilities.db.db_manager import dbManager

# catalog blueprint definition
catalog = Blueprint('catalog', __name__, static_folder='static', static_url_path='/catalog', template_folder='templates')


# Routes
@catalog.route('/catalog')
def index():
    if 'sku' in request.args:       #sku? or name?
        category_code = request.args['sku']
        query_result = dbManager.fetch('''
            SELECT * FROM product AS p
            JOIN category AS c ON p.category_code = c.category_code
            WHERE p.category_code = %s
            ''', (category_code,))
        if query_result:
            return render_template('catalog.html', product=query_result)
    return render_template('catalog.html')
# return render_template('catalog.html', product = product_data)
