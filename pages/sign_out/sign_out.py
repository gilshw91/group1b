from flask import Blueprint, url_for, session, redirect

# sign_out blueprint definition
sign_out = Blueprint('sign_out', __name__, static_folder='static', static_url_path='/sign_out',
                     template_folder='templates')


@sign_out.route('/sign_out')
def index():
    if session['logged-in']:  # if the user clicked sign out, clear session and go to homepage
        session.clear()
    return redirect(url_for('homepage.index'))