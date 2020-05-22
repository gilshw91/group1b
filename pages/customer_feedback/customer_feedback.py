from flask import Blueprint, render_template

# customer_feedback blueprint definition
customer_feedback = Blueprint('customer_feedback', __name__, static_folder='static', static_url_path='/customer_feedback', template_folder='templates')


# Routes
@customer_feedback.route('/customer_feedback')
def index():
    return render_template('customer_feedback.html')