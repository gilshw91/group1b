from flask import Blueprint, render_template

# Content Manager Blueprint Definition
content_manager = Blueprint('content_manager', __name__, static_folder='static', static_url_path='/content_manager',
                     template_folder='templates')


#  Routes
@content_manager.route('/content_manager')
def index():
    return render_template('content_manager.html')
