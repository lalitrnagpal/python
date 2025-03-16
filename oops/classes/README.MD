> #### This is some module documentation . . . 
```
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
```

> #### This is a sub class extending the above class
```
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
```

> #### Lets test them

```
from sub_product import SubProduct

a = SubProduct()

print(a.get_name())         # 
print(a.get_price())        # 
```

> Output
```
initialized
get_price() of SubProduct
get_name() of Product called
None
get_price() of SubProduct
get_price() of Product called
None
```
