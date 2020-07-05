from flask import Blueprint, render_template, request, url_for, redirect, flash
from entities import Customer, Form
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
    email = request.form.get('email')

    user = Customer().get_user_by_email(email)
    if len(user) == 0:
        flash("Please sign-up first")
        return redirect(url_for('sign_in_registration.index'))
    else:
        new_form = Form()
        new_form.application_date = date
        new_form.subject = subject
        new_form.content = content
        new_form.status = status
        new_form.email_address = email
        new_form.add_form()
        flash("Thank you for your feedback")
        return redirect(url_for('customer_feedback.index'))
