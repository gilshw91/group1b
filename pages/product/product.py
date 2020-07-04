from flask import Blueprint, render_template, session, url_for, redirect, flash
from entities import *
from datetime import datetime
from utilities.db.db_manager import dbManager


# product blueprint definition
product = Blueprint('product', __name__, static_folder='static', static_url_path='/product', template_folder='templates')


# Routes
@product.route('/product', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        product_data = Product().get_product(request.args['id'])
        review_data = Review().get_review_by_pid(request.args['id'])
        # review_data = dbManager.fetch('SELECT * FROM review WHERE id=%s', (request.args['id'],))
        return render_template('product.html', product=product_data[0], review=review_data)
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

@product.route('/add_review', methods=['GET', 'POST'])
def add_review():
    date = datetime.now()
    rank = request.form.get('star')
    content = request.form.get('review')
    email = session['email']
    id = request.args['id'] #This isnt working :(

    new_review = Review()
    new_review.date = date
    new_review.rank = rank
    new_review.content = content
    new_review.email_address = email
    new_review.id = id
    new_review.add_review()
    flash("Thank you for your review")
    return redirect(url_for('product.index'))


#
# @product.route('/product', methods=['GET', 'POST'])
# def add_review():
#



