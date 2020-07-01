from utilities.db.db_manager import dbManager
from flask import request
from flask import flash

class Wrapper:
    def __init__(self):
        pass

    def get_all(self, table):
        sql = 'SELECT * FROM %s'
        return dbManager.fetch(sql, (table,))


class Customer:
    def __init__(self):
        pass

    def get_user_by_email(self, email_address):
        """ Returns the users data where the email fits to
            the inserted value by the user. """
        return dbManager.fetch('SELECT * FROM customer WHERE email_address = %s', (email_address, ))

    def get_user_by_user(self, user):
        """ Returns the users data where the user name fits to
            the inserted value by the user. """
        return dbManager.fetch('SELECT * FROM customer WHERE user = %s', (user, ))

    def get_by_email_password(self, email, password):
        """ Returns the user whom email and password belongs to him """
        sql = 'SELECT * FROM customer WHERE email_address=%s AND password=%s'
        return dbManager.fetch(sql, (email, password))

    def add_customer(self, email_address, user, password, first_name, last_name, country, city, street,
                 number, zip, phone_number):
        """ Add new customer to data base"""
        sql_z = ''' INSERT INTO zips (country, city, street, number, zip) VALUES (%s, %s, %s, %s, %s)'''
        sql_c =   '''
                INSERT INTO customer (email_address, user, password, first_name, last_name, country, city, street,
                 number, phone_number)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
        dbManager.commit(sql_z, (country, city, street, number, zip))
        dbManager.commit(sql_c, (email_address, user, password, first_name,
                                 last_name, country, city, street, number,
                                 phone_number))
        flash('You were successfully Signed-up. now you can Sign in')
        return

    def get_address(self, email_address):
        sql = '''SELECT c.email_address, c.country, c.city, c.street, c.number, z.zip 
                    FROM customer AS c 
                    JOIN zips AS z ON c.country=z.country 
                    AND c.city=z.city AND c.street=z.street AND c.number=z.number 
                    WHERE email_address=%s'''
        return dbManager.fetch(sql, (email_address,))


    def update_address(self, city, street, number, zip):
        dbManager.commit('UPDATE customer SET city = %s, street = %s, number = %s', (city, street, number))
        dbManager.commit('UPDATE zips SET zip = %s', (zip,))

class Category:
    def __init__(self):
        pass

    def get_all(self):
        """ returns a list of all categories """
        sql = 'SELECT * FROM category'
        return dbManager.fetch(sql)


class Product:
    def __init__(self):
        pass

    def get_all(self):
        """ returns a list of all products """
        sql = 'SELECT * FROM product'
        return dbManager.fetch(sql)

    def get_products(self):
        return dbManager.fetch('SELECT * FROM product WHERE category_code=%s', (request.args['category_code'],))

    def get_product(self):
        return dbManager.fetch('SELECT * FROM product WHERE id=%s', (request.args['id'],))


class Order:
    def __init__(self):
        pass

    def get_orders(self, email_address):
        """ returns a list of orders associated to e-mail"""
        sql = '''SELECT o.number, o.date_of_order, o.email_address, i.quantity, p.id, p.name, p.price, p.img
                    FROM `order` AS o 
                    JOIN include AS i ON o.number=i.number 
                    JOIN product AS p ON i.sku=p.id
                    WHERE email_address=%s'''
        return dbManager.fetch(sql, (email_address, ))


class Review:
    def __init__(self):
        pass

    def get_reviews(self, email_address):
        sql = '''SELECT r.date, r.rank, r.content, r.email_address, p.name
                    FROM review AS r 
                    JOIN product AS p ON r.id=p.id 
                    WHERE email_address=%s'''
        return dbManager.fetch(sql, (email_address, ))


class Credit:
    def get_credit(self, email_address):
        return dbManager.fetch('SELECT * FROM credit WHERE email_address = %s', (email_address, ))

