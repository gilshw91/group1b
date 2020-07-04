from utilities.db.db_manager import dbManager
from flask import request
from flask import flash


class Customer:
    def __init__(self):
        self.email_address = ""
        self.user = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        self.country = ""
        self.city = ""
        self.street = ""
        self.number = 0
        self.zip = 0
        self.phone_number = 0


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
        """Return the password of user by his email address"""
        sql = 'SELECT password FROM customer WHERE email_address = %s'
        print(dbManager.fetch(sql, (email, ))[0].password)
        return dbManager.fetch(sql, (email, ))[0].password

    def change_password(self, new_password, email):
        """Changes users password by his email address"""
        sql = 'UPDATE customer SET password = %s WHERE email_address = %s'
        dbManager.commit(sql, (new_password, email))
        return

    def add_customer(self):
        """ Add new customer to data base"""
        sql_z = ''' INSERT INTO zips (country, city, street, number, zip) VALUES (%s, %s, %s, %s, %s)'''
        sql_c = '''
                INSERT INTO customer (email_address, user, password, first_name, last_name, country, city, street,
                                      number, phone_number)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
        dbManager.commit(sql_z, (self.country, self.city, self.street, self.number, self.zip))
        dbManager.commit(sql_c, (self.email_address, self.user, self.password, self.first_name, self.last_name,
                                 self.country, self.city, self.street, self.number, self.phone_number))
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

    def update_address(self, country, city, street, number, email):
        """Method that updates the address of the user. by adding new row in 'zips' table
         and than changes the address in 'customer' table where its fit to the zips table."""
        sql_1 = '''
                    INSERT INTO zips (country, city, street, number) 
                    VALUES (%s, %s, %s, %s)
                '''
        sql_2 = '''
                    UPDATE customer SET country=%s, city=%s, street=%s, number=%s
                    WHERE email_address=%s
                '''
        dbManager.commit(sql_1, (country, city, street, number))
        dbManager.commit(sql_2, (country, city, street, number, email))
        flash('Your address has successfully updated!')
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
        # self.id = 0
        # self.name = ""
        # self.price = 0.0
        # self.prev_price = 0.0
        # self.description = ""
        # self.img = ""
        # self.category_code = 0
        pass


    def get_all(self):
        """ returns a list of all products """
        sql = 'SELECT * FROM product'
        return dbManager.fetch(sql)

    def get_products(self):

        return dbManager.fetch('SELECT * FROM product WHERE category_code=%s', (request.args['category_code'],))
        # return dbManager.fetch('SELECT * FROM product WHERE category_code=%s', (self.category_code'],))

    def get_product(self, id):
        # return dbManager.fetch('SELECT * FROM product WHERE id=%s', (request.args['id'],))  # self.id
        return dbManager.fetch('SELECT * FROM product WHERE id=%s', (id,))
        # return dbManager.fetch('SELECT * FROM product WHERE id=%s', (self.id, ))


class Review:
    def __init__(self):
        self.review_number = 0
        self.date = ""
        self.rank = 0
        self.content = ""
        self.email_address = ""
        self.id = 0

    def add_review(self):
        """ Add new review to data base"""
        sql = '''
                INSERT INTO review (review_number, date, `rank`, content, email_address, id)
                VALUES (%s, %s, %s, %s, %s, %s)
              '''
        dbManager.commit(sql, (self.review_number, self.date, self.rank, self.content, self.email_address, self.id))
        return

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

    def get_review_by_pid(self, pid):
        """ This method returns the reviews on product
        by it's id. """
        sql = 'SELECT * FROM review WHERE id=%s'
        print(dbManager.fetch(sql, (pid,)))
        return dbManager.fetch(sql, (pid, ))

    def recent_reviews(self, email):
        """Returns the top three recent reviews that the user has posted"""
        sql = ''' 
                SELECT r.date, r.rank, r.content, r.email_address, p.name
                FROM review AS r 
                JOIN product AS p 
                ON r.id = p.id 
                WHERE email_address = %s
                ORDER BY r.date DESC 
                LIMIT 3
              '''
        return dbManager.fetch(sql, (email, ))


class Credit:
    def __init__(self):
        self.credit_number = 0
        self.exp = ""
        self.cvv = 0
        self.email_address = ""

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

    def add_credit(self):
        """if the user doesnt have a credit in the database
        this method will insert the credit data by the users' email"""
        sql = '''
                INSERT INTO credit (credit_card_number, expiration_date, cvv, email_address)
                VALUES (%s, %s, %s, %s)
              '''
        dbManager.commit(sql, (self.credit_number, self.exp, self.cvv, self.email_address))
        return

    def delete_credit(self, email):
        """Methods that deletes the user's credit card by the user's email"""
        return dbManager.commit('DELETE FROM credit WHERE email_address=%s', (email,))

class Order:
    def __init__(self):
        pass

    def get_history(self, email):
        """This method returns the history of all the orders (their details) and the products
            which the user submitted on."""
        sql = '''
                SELECT o.number, o.date_of_order, o.email_address, i.quantity, p.id ,p.name, p.price, p.img
                FROM orders AS o 
                JOIN include AS i ON o.number = i.number
                JOIN product AS p ON i.sku = p.id
                WHERE email_address = %s
                 # ORDER BY o.date_of_order DESC 
              '''
        return dbManager.fetch(sql, (email,))

    def get_orders(self, email_address):
        """ returns a list of orders associated to e-mail"""
        sql = '''SELECT o.number, o.date_of_order, o.email_address, i.quantity, p.id, p.name, p.price, p.img
                       FROM orders AS o 
                       JOIN include AS i ON o.number=i.number 
                       JOIN product AS p ON i.sku=p.id
                       WHERE email_address=%s'''
        return dbManager.fetch(sql, (email_address,))

class Form:
    def __init__(self):
        self.application_number = 0
        self.application_date = ""
        self.subject = ""
        self.content = ""
        self.status = ""
        self.email_address = ""

    def add_form(self):
        """ Add new feedback form to data base"""
        sql = '''
                INSERT INTO form (application_number, application_date, subject, content, status, email_address)
                VALUES (%s, %s, %s, %s, %s, %s)
              '''
        dbManager.commit(sql, (self.application_number, self.application_date, self.subject, self.content, self.status, self.email_address))
        return