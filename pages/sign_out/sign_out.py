from flask import Blueprint, render_template, url_for, session, redirect
from utilities.db.db_manager import dbManager

# sign_out blueprint definition
sign_out = Blueprint('sign_out', __name__, static_folder='static', static_url_path='/sign_out', template_folder='templates')


@sign_out.route('/sign_out')
def index():
    if session['logged-in']:  # if the user clicked sign out, clear and go to homepage
        # session['logged-in'] = False
        session.clear()
    return redirect(url_for('homepage.index'))