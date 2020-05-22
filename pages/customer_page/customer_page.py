from flask import Blueprint, render_template

# customer_page blueprint definition
customer_page = Blueprint('customer_page', __name__, static_folder='static', static_url_path='/customer_page', template_folder='templates')


# Routes
@customer_page.route('/customer_page')
def index():
    return render_template('customer_page.html')