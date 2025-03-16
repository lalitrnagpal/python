"""This is some module documentation"""
from product import Product

class SubProduct(Product):
    """This is some class level documentation"""
    def __init__(self):
        super().__init__()
        print('initialized')

    def get_price(self):
        print('get_price() of SubProduct')
        return super().get_price()
    
    def get_name(self):
        print('get_price() of SubProduct')
        return super().get_name()