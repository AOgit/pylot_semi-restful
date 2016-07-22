"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('Product')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        all_products = self.models['Product'].get_all_products()
        return self.load_view('index.html', all_products=all_products)

    def new(self):
        return self.load_view('add_prod.html')

    def edit(self, id):
        product = self.models['Product'].show_product(id)
        return self.load_view('edit_prod.html', product=product[0])

    def update(self, id, method='POST'):
        a = request.form
        product = self.models['Product'].update_product(id,a)
        return redirect('/')

    def show(self, id):
        product = self.models['Product'].show_product(id)
        return self.load_view('show.html', product=product[0])

    def create(self):
        b = request.form
        product = self.models['Product'].create_product(b)
        if product['status'] == True:
            product = product['prod']
            return redirect('/')
        else:
            for message in product['errors']:
                flash(message)
            return self.load_view('add_prod.html')

    def destroy(self, id, method='POST'):
        product = self.models['Product'].delete_product(id)
        return redirect('/')


