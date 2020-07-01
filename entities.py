from utilities.db.db_manager import dbManager
from flask import flash

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
        flash('You were successfully Signed-up now you can Sign in')
        return


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