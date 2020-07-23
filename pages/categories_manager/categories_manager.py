from flask import Blueprint, render_template, redirect, url_for, request, flash
from entities import Category

# Categories Blueprint Definition
categories_manager = Blueprint('categories_manager', __name__, static_folder='static', static_url_path='/categories_manager',
                     template_folder='templates')


#  Routes
@categories_manager.route('/categories_manager')
def index():
    categories_data = Category().get_all()
    return render_template('categories_manager.html', categories=categories_data)


@categories_manager.route('/add_category', methods=["POST"])
def add_category():
    category = Category()
    category.category_code = request.form['category-code']
    category.category_name = request.form['category-name']
    category.img = request.form['img']
    category.add_category()
    flash('Added Successfully!')
    return redirect(url_for('categories_manager.index'))


@categories_manager.route('/update', methods=["POST"])
def update():
    Category().update_category(request.form['category-code'], request.form['category-name'], request.form['img'])
    flash('Updated Successfully!')
    return redirect(url_for('categories_manager.index'))


@categories_manager.route('/delete/<string:category_code>', methods=["GET"])
def delete(category_code):
    Category().delete_category(category_code)
    flash('Deleted Successfully!')
    return redirect(url_for('categories_manager.index'))

