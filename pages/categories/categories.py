from flask import Blueprint, render_template
from utilities.db.db_manager import dbManager

# categories blueprint definition
categories = Blueprint('categories', __name__, static_folder='static', static_url_path='/categories', template_folder='templates')


# Routes
@categories.route('/categories')
def index():
    category_data = dbManager.fetch('SELECT * FROM category')
    return render_template('categories.html', categories = category_data)