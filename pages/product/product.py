from flask import Blueprint, render_template

# product blueprint definition
product = Blueprint('product', __name__, static_folder='static', static_url_path='/product', template_folder='templates')


# Routes
@product.route('/extendable_ears')
def extendable_ears():
    return render_template('extendable_ears.html')


@product.route('/peruvian_instant_darkness_powder')
def peruvian_instant_darkness_powder():
    return render_template('peruvian_instant_darkness_powder.html')
