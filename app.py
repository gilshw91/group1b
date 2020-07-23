from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)

## Categories
from pages.categories.categories import categories
app.register_blueprint(categories)

## sign_in_registration
from pages.sign_in_registration.sign_in_registration import sign_in_registration
app.register_blueprint(sign_in_registration)

## sign_up
from pages.sign_up.sign_up import sign_up
app.register_blueprint(sign_up)

## sign_out
from pages.sign_out.sign_out import sign_out
app.register_blueprint(sign_out)

# Product
from pages.product.product import product
app.register_blueprint(product)

## catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## customer_feedback
from pages.customer_feedback.customer_feedback import customer_feedback
app.register_blueprint(customer_feedback)

##customer_page
from pages.customer_page.customer_page import customer_page
app.register_blueprint(customer_page)
###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

## cart
from pages.cart.cart import cart
app.register_blueprint(cart)

## content_manager
from pages.content_manager.content_manager import content_manager
app.register_blueprint(content_manager)