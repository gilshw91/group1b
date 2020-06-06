from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
#TODO: we need to change homepage to homepage page
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

# Product check
from pages.product.product import product
app.register_blueprint(product)

## catalogue
from pages.catalogue.catalogue import catalogue
app.register_blueprint(catalogue)

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
