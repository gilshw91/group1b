from utilities.db.db_manager import dbManager
from flask import flash

class Customer:
    def __init__(self, email_address, user, password, first_name, last_name, country, city, street,
                 number, zip, phone_number):
        self.email_address = email_address
        self.user = user
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.city = city
        self.street = street
        self.number = number
        self.zip = zip
        self.phone_number = phone_number

    def get_user_by_email(self):
        """ Returns the users data where the email fits to
            the inserted value by the user. """
        return dbManager.fetch('SELECT * FROM customer WHERE email_address = %s', (self.email_address, ))

    def get_user_by_user(self):
        """ Returns the users data where the user name fits to
            the inserted value by the user. """
        return dbManager.fetch('SELECT * FROM customer WHERE user = %s', (self.user, ))

    def add_customer(self):
        """ Add new customer to data base"""
        sql_z = ''' INSERT INTO zips (country, city, street, number, zip) VALUES (%s, %s, %s, %s, %s)'''
        sql_c =   '''
                INSERT INTO customer (email_address, user, password, first_name, last_name, country, city, street,
                 number, phone_number)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
        dbManager.commit(sql_z, (self.country, self.city, self.street, self.number, self.zip))
        dbManager.commit(sql_c, (self.email_address, self.user, self.password, self.first_name,
                                 self.last_name, self.country, self.city, self.street, self.number,
                                 self.phone_number))
        flash('You were successfully Signed-up now you can Sign in')
        return


class Category:
    def __init__(self):
        pass

    def get_all(self):
        """ returns a list of all categories """
        sql = 'SELECT * FROM category'
        return dbManager.fetch(sql)
