from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from entities import *
from datetime import datetime
from utilities.db.db_manager import dbManager
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
    if request.method == 'GET': #Regular version
        product_data = Product().get_product(request.args['id'])
        review_data = Review().get_review(request.args['id'])
        session['pid'] = request.args['id']
        if len(review_data):
            return render_template('product.html', product=product_data[0], review=review_data[0])
        else:
            return render_template('product.html', product=product_data[0])
    else: #After review was given
        if not session.get('logged-in'):
            flash("Please sign-in to post a review")
            return redirect(url_for('sign_in_registration.index'))
        else:
            email = session['email']
            review = request.form.get('review')
            pid = session['pid']
            rank = request.form.get('star')
            dt_string = datetime.now()#.strftime("%d-%m-%Y %H:%M:%S")  # dd-mm-YY H:M:S
            new_review = Review()
            new_review.date = dt_string
            new_review.rank = rank
            new_review.content = review
            new_review.email_address = email
            new_review.id = pid
            new_review.add_review()
            flash("Thank you for your review")
            return redirect(url_for('homepage.index'))







