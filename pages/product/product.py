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
        product_data = Product().get_product()
        review_data = Review().get_review()
        return render_template('product.html', product=product_data[0], review=review_data[0])
    else: #After review was given
        email = request.form.get('email')
        review = request.form.get('review')
        product = Product().get_product()
        pid = product.id
        rank = request.form.get('star')
        dt_string = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  # dd-mm-YY H:M:S
        if session.get('logged-in'):
            if email == session['email']:
                new_review = Review()
                new_review.date = dt_string
                new_review.rank = rank
                new_review.content = review
                new_review.email_address = email
                new_review.id = pid
                new_review.add_review()
                flash("Thank you for your review")
                return redirect(url_for('product.index'))
            return render_template('product.html', product=pid)
        flash("You should sign-in to post a review")

#@product.route('/add_review', methods=['GET', 'POST'])
#def add_review():
#    date = datetime.now()
#    rank = request.form.get('star')
#    content = request.form.get('review')
#    email = session['email']
#    id = request.args['id'] #This isnt working :(

#   new_review = Review()
#   new_review.date = date
#    new_review.rank = rank
#    new_review.content = content
#    new_review.email_address = email
#    new_review.id = id
#    new_review.add_review()
#    flash("Thank you for your review")
#    return redirect(url_for('product.index'))


#
# @product.route('/product', methods=['GET', 'POST'])
# def add_review():
#



