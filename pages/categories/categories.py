from flask import Blueprint, render_template
from entities import Category

# categories blueprint definition
categories = Blueprint('categories', __name__, static_folder='static', static_url_path='/categories', template_folder='templates')


# Routes
@categories.route('/categories')
def index():
    categories_data = Category().get_all()
    return render_template('categories.html', categories=categories_data)


@categories.route('/content_manager')
def content_manager():
    return render_template('content_manager.html')
