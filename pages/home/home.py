from flask import Blueprint, render_template, redirect, url_for

# home blueprint definition
home = Blueprint('home', __name__, static_folder='static', static_url_path='/home', template_folder='templates')


# Routes
@home.route('/')
def index():
    return render_template('home.html')


@home.route('/home')
def redirect_home():
    return redirect(url_for('home.index'))
