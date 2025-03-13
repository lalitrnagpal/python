""" This is some module documentation . . . """
from abc import ABC, abstractmethod

class Product(ABC):
    """ This is some class level documentation . . . """

    @abstractmethod
    def get_price(self):
        """ This is some method level documentation . . . """
        print("get_price() of Product called")

    @abstractmethod
    def get_name(self):
        """ This is some method level documentation . . . """
        print("get_name() of Product called")
