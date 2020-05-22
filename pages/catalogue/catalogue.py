from flask import Blueprint, render_template

# categories blueprint definition
categories = Blueprint('catalogue', __name__, static_folder='static', static_url_path='/catalogue', template_folder='templates')


# Routes
@categories.route('/catalogue')
def index():
    return render_template('catalogue.html')