from flask import Blueprint, render_template

# product blueprint definition
product = Blueprint('product', __name__, static_folder='static', static_url_path='/product', template_folder='templates')


# Routes
@product.route('/product')
def index():
    return render_template('product.html')
