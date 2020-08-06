from flask import Blueprint, render_template, redirect, url_for, request, flash
from entities import Category, Product

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
    if not request.form['category-code'].isdigit():
        flash("Category Code must be an integer. Try again!")
        return redirect(url_for('categories_manager.index'))
    category = Category()
    category.category_code = request.form['category-code']
    category.category_name = request.form['category-name']
    category.img = request.form['img']
    category.add_category()
    flash('Added Successfully!')
    return redirect(url_for('categories_manager.index'))


@categories_manager.route('/update_category', methods=["POST"])
def update_category():
    # Updates another field which isnt the category code
    if request.form['given-code'] != request.form['category-code']:
        # if Category().is_category_code(request.form['category-code']):
        #     flash("Category Code is already exist. Try again!")
        flash("Can't update Category code, You can delete and add new category.")
        return redirect(url_for('categories_manager.index'))

    Category().update_category(request.form['category-code'], request.form['category-name'], request.form['img'])
    flash('Updated Successfully!')
    return redirect(url_for('categories_manager.index'))


@categories_manager.route('/delete_category/<string:category_code>', methods=["GET"])
def delete_category(category_code):
    if Product().is_product_by_category_code(category_code):
        flash("There is a Product in this Category, Deleted Failed!")
        flash("You can delete this product from 'Product Page'")
        return redirect(url_for('categories_manager.index'))
    Category().delete_category(category_code)
    flash('Deleted Successfully!')
    return redirect(url_for('categories_manager.index'))

