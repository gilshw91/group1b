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

    def get_password(self, email):
        sql = 'SELECT password FROM customer WHERE email_address = %s'
        return dbManager.fetch(sql, (email, ))

    def change_password(self, new_password, email):
        sql = 'UPDATE customer SET password = %s WHERE email_address = %s'
        dbManager.commit(sql, (new_password, email))
        flash("Changed successfully")
        return

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

    def get_address(self, email):
        """ Returns the full address of a user, which identify by his email"""
        sql = '''
                SELECT c.email_address, c.country, c.city, c.street, c.number, z.zip 
                FROM customer AS c 
                JOIN zips AS z ON c.country=z.country 
                AND c.city=z.city AND c.street=z.street AND c.number=z.number 
                WHERE email_address=%s
              '''
        return dbManager.fetch(sql, (email, ))

    def update_address(self, country, city, street, number, zip, email):
        sql_1 = '''
                    UPDATE customer SET country =%s, city = %s, street = %s, number = %s
                    WHERE email_address = %s
                '''
        sql_2 = '''
                    UPDATE zips SET  zip = %s
                    WHERE country = %s AND city = %s AND street = %s AND number = %s
                '''
        dbManager.commit(sql_1, (country, city, street, number, email))
        dbManager.commit(sql_2, (zip, country, city, street, number, email))
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

class Review:
    def __init__(self):
        pass

    def get_review_by_email(self, email):
        """ This method returns the reviews on product
        which was submitted by user (his email address). """
        sql = ''' 
                SELECT r.date, r.rank, r.content, r.email_address, p.name
                FROM review AS r 
                JOIN product AS p 
                ON r.id = p.id 
                WHERE email_address = %s
              '''
        return dbManager.fetch(sql, (email, ))


class Credit:
    def __init__(self):
        pass

    def get_credit_by_email(self, email):
        """Return the credit data by the user email"""
        sql = 'SELECT * FROM credit WHERE email_address = %s'
        return dbManager.fetch(sql, (email,))

    def update_credit(self, credit_number, exp, cvv, email):
        """updates and changes a credit data by the users' email"""
        sql = '''
                UPDATE credit SET credit_card_number = %s, expiration_date = %s, cvv = %s
                WHERE email_address = %s
              '''
        dbManager.commit(sql, (credit_number, exp, cvv, email))
        return

    def add_credit(self, credit_number, exp, cvv, email):
        """if the user doesnt have a credit in the database
        this method will insert the credit data by the users' email"""
        sql = '''
                INSERT INTO credit (credit_card_number, expiration_date, cvv, email_address)
                VALUES (%s, %s, %s, %s)
              '''
        dbManager.commit(sql, (credit_number, exp, cvv, email))
        return


class Order:
    def __init__(self):
        pass

    def get_history(self, email):
        """This method returns the history of all the orders (their details) and the products
            which the user submitted on."""
        sql = '''
                SELECT o.number, o.date_of_order, o.email_address, i.quantity, p.id,p.name, p.price, p.img
                FROM 'order' AS o 
                JOIN include AS i ON o.number = i.number 
                JOIN product AS p ON i.sku = p.id
                WHERE email_address = %s
                # ORDER BY o.date_of_order DESC 
              '''
        return dbManager.fetch(sql, (email,))
