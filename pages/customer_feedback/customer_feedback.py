from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from entities import *
from datetime import datetime

# customer_feedback blueprint definition
customer_feedback = Blueprint('customer_feedback', __name__, static_folder='static', static_url_path='/customer_feedback', template_folder='templates')


# Routes
@customer_feedback.route('/customer_feedback')
def index():
        return render_template('customer_feedback.html', methods=['GET', 'POST'])


@customer_feedback.route('/add_form', methods=['POST'])
def add_form():

    date = datetime.now()
    subject = request.form.get('subject')
    content = request.form.get('message')
    status = 'unread'
    email = session['email']

    new_form = Form()
    new_form.application_date = date
    new_form.subject = subject
    new_form.content = content
    new_form.status = status
    new_form.email_address = email
    new_form.add_form()
    flash("Thank you for your feedback")
    return redirect(url_for('customer_feedback.index'))
