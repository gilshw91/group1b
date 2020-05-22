from flask import Blueprint, render_template

# catalogue blueprint definition
catalogue = Blueprint('catalogue', __name__, static_folder='static', static_url_path='/catalogue', template_folder='templates')


# Routes
@catalogue.route('/catalogue')
def index():
    return render_template('catalogue.html')