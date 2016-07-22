""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def get_all_products(self):
        query = "SELECT * FROM products"
        return self.db.query_db(query)

    def show_product(self, id):
        query = "SELECT * FROM products WHERE id = :id"
        data = {'id':id}
        return self.db.query_db(query, data)

    def update_product(self, id, a):
        query = "UPDATE products SET name=:name, description=:description, price=:price WHERE id=:id"
        values = {'name':a['prod_name'], 'description':a['prod_desc'], 'price':a['prod_price'], 'id':id}
        return self.db.query_db(query, values)

    def create_product(self, b):
        errors = []
        if not b['prod_name']:
            errors.append('Product name cannot be blank.')
        if not b['prod_price']:
            errors.append('Price cannot be blank.')
        elif b['prod_price'].isalpha():
            errors.append('Product has to be a numeric value!')

        if errors:
            return {"status": False, "errors": errors}
        else:
            query = "INSERT INTO products (name, description, price) VALUES (:name, :description, :price)"
            values = {'name':b['prod_name'], 'description':b['prod_desc'], 'price': b['prod_price']}
            prods = self.db.query_db(query, values)
            return {"status": True, "prod": prods}

    def delete_product(self, id):
        query = "DELETE FROM products WHERE id=:id"
        values = {'id':id}
        return self.db.query_db(query, values)

    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """