from flask import Blueprint, render_template, request, session, url_for, flash
from utilities.db.db_manager import dbManager
from datetime import datetime
#
# start_counter = datetime.datetime(2020, 6, 28, 0, 30)  # june 6th 2020, 0from 00:30 am
#
#
# def get_counter(when):
#     return (when - start_counter).days
# # get_counter(datetime.datetime(2020,6,28,0,45)) will return 0
#
# session['counter'] = 0  # needs to be reset everyday

# product blueprint definition
product = Blueprint('product', __name__, static_folder='static', static_url_path='/product', template_folder='templates')


# Routes
@product.route('/product', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        product_data = dbManager.fetch('SELECT * FROM product WHERE id=%s', (request.args['id'],))
        review_data = dbManager.fetch('SELECT * FROM review WHERE id=%s', (request.args['id'],))
        return render_template('product.html', product=product_data[0], review=review_data[0])
    else:
        email = request.form.get('email')
        review = request.form.get('review')
        pid = dbManager.fetch('SELECT * FROM product WHERE id=%s', (request.args['id'],))
        # pid = product.id # Fetching?
        rank = request.form.get('star')
        dt_string = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  # dd-mm-YY H:M:S
        if session.get('logged-in'):
            if email == session['email']:
                dbManager.commit("INSERT INTO review ('review_number', 'date', 'rank', 'content', 'email_address', 'id') \
                                 VALUES(%s, %s, %s, %s, %s, %s)", (0, dt_string, rank, review, email, pid))
            return render_template('product.html', product=pid)
        flash("You should sign-in to post a review")

#
# @product.route('/product', methods=['GET', 'POST'])
# def add_review():
#



