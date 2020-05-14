from flask import Blueprint, render_template

# sign_in_registration blueprint definition
sign_in_registration = Blueprint('sign_in_registration', __name__, static_folder='static', static_url_path='/sign_in_registration', template_folder='templates')


# Routes
@sign_in_registration.route('/sign_in_registration')
def index():
    return render_template('sign_in_registration.html')
