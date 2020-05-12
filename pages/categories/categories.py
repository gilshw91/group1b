from flask import Blueprint, render_template

# categories blueprint definition
categories = Blueprint('categories', __name__, static_folder='static', static_url_path='/categories', template_folder='templates')


# Routes
@about.route('/categories')
def index():
    return render_template('categories.html')
