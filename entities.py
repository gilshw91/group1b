from utilities.db.db_manager import dbManager
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
        # self.zip = 0
        self.phone_number = 0

    def get_all(self):
        """ Returns all users data from database """
        return dbManager.fetch('SELECT * FROM customer')

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
        return dbManager.fetch(sql, (email, ))[0].password

    def change_password(self, new_password, email):
        """Changes users password by his email address"""
        sql = 'UPDATE customer SET password = %s WHERE email_address = %s'
        dbManager.commit(sql, (new_password, email))
        return

    def add_customer(self):
        """ Add new customer to data base"""
        # sql_z = ''' INSERT INTO zips (country, city, street, number, zip) VALUES (%s, %s, %s, %s, %s)'''
        sql_c = '''
                INSERT INTO customer (email_address, user, password, first_name, last_name, country, city, street,
                                      number, phone_number)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
        # dbManager.commit(sql_z, (self.country, self.city, self.street, self.number, self.zip))
        dbManager.commit(sql_c, (self.email_address, self.user, self.password, self.first_name, self.last_name,
                                 self.country, self.city, self.street, self.number, self.phone_number))
        return

    def get_address(self, email):
        """ Returns the full address of a user, which identify by his email"""
        sql = '''
                SELECT c.email_address, c.country, c.city, c.street, c.number 
                #, z.zip 
                FROM customer AS c 
                # JOIN zips AS z ON c.country=z.country 
                # AND c.city=z.city AND c.street=z.street AND c.number=z.number 
                WHERE email_address=%s
              '''
        return dbManager.fetch(sql, (email, ))

    def update_address(self, country, city, street, number, email):
        """Method that updates the address of the user. by adding new row in 'zips' table
         and than changes the address in 'customer' table where its fit to the zips table."""
        # sql_1 = '''
        #             INSERT INTO zips (country, city, street, number)
        #             VALUES (%s, %s, %s, %s)
        #         '''
        sql_2 = '''
                    UPDATE customer SET country=%s, city=%s, street=%s, number=%s
                    WHERE email_address=%s
                '''
        # dbManager.commit(sql_1, (country, city, street, number))
        dbManager.commit(sql_2, (country, city, street, number, email))
        flash('Your address has successfully updated!')
        return

    def delete_customer(self, email):
        dbManager.commit('DELETE FROM customer WHERE email_address=%s', (email,))
        return


class Category:
    def __init__(self):
        pass

    def get_all(self):
        """ returns a list of all categories """
        sql = 'SELECT * FROM category'
        return dbManager.fetch(sql)

    def add_category(self):
        """ Method that insert a new Category to DB """
        sql = '''
                    INSERT INTO category (category_code, category_name, img)
                    VALUES (%s, %s, %s)
              '''
        dbManager.commit(sql, (self.category_code, self.category_name, self.img))
        return

    def update_category(self, category_code, category_name, img):
        """ Method that update an existing category by the category' code"""
        sql = '''  
                    UPDATE category SET category_code = %s, category_name = %s, img =%s
                    WHERE category_code = %s
              '''
        dbManager.commit(sql, (category_code, category_name, img, category_code))
        return

    def delete_category(self, category_code):
        """ Method that delete category form DB by the category code """
        return dbManager.commit('DELETE FROM category WHERE category_code=%s', (category_code,))

class Product:
    def __init__(self):
        id = 0
        name = ""
        price = 0
        prev_price = 0
        description = ""
        img = ""
        category_code = 0

    def get_all(self):
        """ returns a list of all products """
        sql = 'SELECT * FROM product'
        return dbManager.fetch(sql)

    def get_products(self, id):
        """ returns the products that belongs to specific category"""
        return dbManager.fetch('SELECT * FROM product WHERE category_code=%s', (id,))

    def get_product(self, id):
        """Returns the product with the given id"""
        return dbManager.fetch('SELECT * FROM product WHERE id=%s', (id,))

    def add_product(self):
        """ Method that insert a new product to DB """
        sql = '''
            INSERT INTO product (id, name, price, description, img, category_code)
            VALUES (%s, %s, %s, %s, %s, %s)
            '''
        dbManager.commit(sql, (self.id, self.name, self.price, self.description,
                               self.img, self.category_code))
        return

    def update_product(self, id, name, price, prev_price, description, img, category_code, given_id):
        """ Method that update an existing product by the products' current ID """
        sql = '''  
                    UPDATE product SET id = %s, name = %s, price =%s, prev_price = %s,
                    description = %s, img = %s, category_code = %s
                    WHERE id = %s
              '''
        if id != given_id:
            include_data = dbManager.fetch('SELECT * FROM include WHERE sku=%s', (given_id,))
            if include_data:
                print(include_data)
                quantity = include_data[0].quantity
                number = include_data[0].number
                print("1")
                dbManager.commit('DELETE FROM include WHERE sku=%s', (given_id,))
                print("2")
                print("5")
                dbManager.commit(sql, (id, name, price, prev_price, description, img, category_code, given_id))
                print("6")
                sql_include = ''' 
                                INSERT INTO include (quantity, number, sku)
                                VALUES (%s, %s, %s)
                              '''
                dbManager.commit(sql_include, (quantity, number, id))
        print("4")
        dbManager.commit(sql, (id, name, price, prev_price, description, img, category_code, given_id))
        print("444")
        return

    def delete_product(self, id):
        """ Method that delete product form DB by the products' ID """
        return dbManager.commit('DELETE FROM product WHERE id=%s', (id,))

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

    def get_review(self, id):
        """Returns the review which the id is associated with"""
        return dbManager.fetch('SELECT * FROM review WHERE id=%s', (id,))

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
        """Updates and changes a credit data by the users' email"""
        sql = '''
                UPDATE credit SET credit_card_number = %s, expiration_date = %s, cvv = %s
                WHERE email_address = %s
              '''
        dbManager.commit(sql, (credit_number, exp, cvv, email))
        return

    def add_credit(self):
        """If the user doesnt have a credit in the database
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
              '''
        return dbManager.fetch(sql, (email,))

    def get_product_order(self, email_address, id):
        """ returns a specific product from orders associated to e-mail"""
        sql = '''SELECT o.number, o.date_of_order, o.email_address, i.quantity, p.id, p.name, p.price, p.img
                       FROM orders AS o 
                       JOIN include AS i ON o.number=i.number 
                       JOIN product AS p ON i.sku=p.id
                       WHERE email_address=%s AND id=%s'''
        return dbManager.fetch(sql, (email_address, id))


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
        dbManager.commit(sql, (self.application_number, self.application_date, self.subject, self.content, self.status,
                               self.email_address))
        return


# class Manager:
#     def __init__(self):
#         pass
#
#     def get_tables_names(self):
#         table1 = 'Products'
#         table2 = 'Categories'
#         return