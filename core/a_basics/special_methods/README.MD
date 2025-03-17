# Special Methods / Dunder / Magic Methods

> A class may define or inherit **special methods**, often referred to as **"dunder” methods"**, called so as their names have **leading and trailing double underscores**  

> Python **implicitly calls a special method whenever you perform the related operation** on an **instance object**

> Whenever we mention calls to **x.\_\_whatever\_\_(...)**, keep in mind that the exact call happening is rather, pedantically speaking, **x.\_\_class\_\_.\_\_whatever\_\_(x, ...)**.

#### Initialization and finalization

A class can control its **instance's initialization** (a very common requirement) via special methods **\_\_new\_\_** and **\_\_init\_\_**, and/or their **finalization** (a rare requirement) via **\_\_del\_\_**.

> What happens if __new__ does not return an instance?

```
class A:
    def __new__(cls):
        print("Creating instance")

    def __init__(self):
        print("Initializing instance")

print(A())

# Output: 
Creating instance
None
```

> Returning a different type from __new__

```
class A:
    def __new__(cls):
        print("Creating instance")
        return "Hello, World!"

print(A())
```

> Returning an instances of another class

```
class GeeksforGeeks:
    def __str__(self):
        return "GeeksforGeeks Instance"

class Geek:
    def __new__(cls):
        return GeeksforGeeks()
    
    def __init__(self):
        print("Inside init")

print(Geek())

# Output: GeeksforGeeks Instance
```

> **String representation**

A class can control how Python renders its instances as strings via special methods **\_\_repr\_\_, \_\_str\_\_, \_\_format\_\_,** and **\_\_bytes\_\_**.

\_\_repr\_\_ magic method is used to represent the instance of a class in string. When we try to print the object of a class the \_\_repr\_\_ method is implicitly invoked that returns a string


```
__str__(self): Defines behavior for when str() is called on an instance of your class.

__repr__(self): To get called by built-int repr() method to return a machine readable representation of a type.

    # Python program to demonstrate writing of __repr__ and __str__ for user defined classes

    # A user defined class to represent Complex numbers 
    
    class Complex:

	    # Constructor
	    def __init__(self, real, imag):
	        self.real = real
	        self.imag = imag

	    # For call to repr(). Prints object's information
	    def __repr__(self):
	        return 'Rational(%s, %s)' % (self.real, self.imag) 

	    # For call to str(). Prints readable form
	    def __str__(self):
	        return '%s + i%s' % (self.real, self.imag) 


    # Driver program to test above
    t = Complex(10, 20)

    # Same as "print t"
    print (str(t))

    print (repr(t))

__hash__(self): It has to return an integer, and its result is used for quick key comparison in dictionaries.

    class Emp:
        def __init__(self, emp_name, id):
            self.emp_name = emp_name
            self.id = id

        def __eq__(self, other):
      
            # Equality Comparison between two objects
            return self.emp_name == other.emp_name and self.id == other.id

        def __hash__(self):
      
            # hash(custom_object)
            return hash((self.emp_name, self.id))

    emp = Emp('Ragav', 12)

    print("The hash is: %d" % hash(emp))

    # We'll check if two objects with the same attribute values have the same hash
    emp_copy = Emp('Ragav', 12)

    print("The hash is: %d" % hash(emp_copy))

__format__(self, formatstr): return a new style of string.

__nonzero__(self): Defines behavior for when bool() is called on an instance of your class. 

__dir__(self): This method to return a list of attributes of a class.

__sizeof__(self): It return the size of the object.

__unicode__(self): This method to return an unicode string of a type.

```

> **Comparison, hashing, and use in a Boolean context**

A class can control how its instances compare with other objects (via special methods **\_\_lt\_\_, \_\_le\_\_, \_\_gt\_\_, \_\_ge\_\_, \_\_eq\_\_, and \_\_ne\_\_**), how dictionaries use them as keys and sets use them as members (via **\_\_hash\_\_**), and whether they evaluate as truthy or falsy in Boolean contexts ( via **\_\_bool\_\_**). 

```
class Comparison:
    def __init__(self, a):
        self.a = a
    def __lt__(self, object2):
        return self.a < object2.a
    def __gt__(self, object2):
        return self.a > object2.a
    def __le__(self, object2):
        return self.a <= object2.a
    def __ge__(self, object2):
        return self.a >= object2.a
    def __eq__(self, object2):
        return self.a == object2.a
    def __ne__(self, object2):
        return self.a != object2.a

a = Comparison(1)

b = Comparison(2)

print(
    a < b,
    a > b,
    a <= b,
    a >= b,
    a == b,
    a != b
)
```

> **Attribute reference, binding, and unbinding**

A class can control access to its instances’ attributes (reference, binding, unbinding) via special methods **\_\_getattribute\_\_, \_\_getattr\_\_, \_\_setattr\_\_, and \_\_delattr\_\_**.



> **Callable instances**

A class can make its instances callable, just like function objects, via special method **\_\_call\_\_**.

```
class CallExample:
    def __init__(self, val):
        self.val = val
    def __call__(self, b):
        return self.val * b

call_example = CallExample(5)

print(call_example(6))

# Output: 30
```

> \_\_getitem\_\_ and \_\_setitem\_\_ magic method

\_\_getitem\_\_ method is used to get an item from the invoked instances’ attribute. \_\_getitem\_\_ is commonly used with containers like list, tuple, etc.

```
class A:
    def __init__(self, item):
        self.item = item
    def __getitem__(self, index):
        return self.item[index]

a = A([1, 2, 3])

print(f"First item: {a[0]}")
print(f"Second item: {a[1]}")
print(f"Third item: {a[2]}")

# Output: 
# First item: 1
# Second item: 2
# Third item: 3
```

\_\_setitem\_\_ method is used to set the item into a specific index of the invoked instances’ attribute. Similar to \_\_getitem\_\_, \_\_setitem\_\_ is also used with containers.

```
class SetItemExample:
    def __init__(self, item):
        self.item = item
    def __setitem__(self, index, item1):
        self.item[index] = item1

setitem_instance = SetItemExample([1, 2, 3])
print(f"Items before setting: {setitem_instance.item}")

setitem_instance[1] = 5
print(f"Items after setting: {setitem_instance.item}")

# Output
# Items before setting: [1, 2, 3]
# Items after setting: [1, 5, 3]
```

> **\_\_len\_\_ magic method**

\_\_len\_\_ magic method is used to find the length of the instance attributes. When we use len(instance), it returns the length of the instance attribute which is usually containers.

When we invoke the len() method the length of the list named item is returned that is defined inside the \_\_len\_\_ method.

```
class LenExample:
    def __init__(self, item):
        self.item = item
    def __len__(self):
        return len(self.item)

len_instance = LenExample([1, 2, 3])

print( len( len_instance ) )
# Output: 3
```

> **\_\_contains\_\_ method**

\_\_contains\_\_ method is invoked when using the membership operator ‘in’. When we want to check whether an element is present in the object’s attributes that are usually container (lists, tuple) we can use the \_\_contains\_\_ method.

```
class ContainsExample:
    def __init__(self, items):
        self.items = items
    def __contains__(self, item):
        return item in self.items

contains_instance = ContainsExample([1, 2, 3, 4, 5])
print(4 in contains_instance)
```

**\_\_enter\_\_ and \_\_exit\_\_ magic methods**

\_\_enter\_\_ and \_\_exit\_\_ methods are used along with the ‘with’ block in python. The ‘with’ block in python is used to open and close the file object or any other objects that have a close method.

```
class WriteFile:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None

    def log(self, text):
        self.file.write(text+'n')

    def __enter__(self):
        self.file = open(self.file_name, "a+")
        return self    

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with WriteFile(r"filename.txt") as log_file:
    log_file.log("Log Test 1")
    log_file.log("Log Test 2")
```

**\_\_iter\_\_ magic method**

\_\_iter\_\_ method is used to provide a generator object for the provided instance. We can make use of iter() and next() method to leverage __iter__ method.

```
class Squares:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

i = iter(Squares(1, 3))

print(next(i))
print(next(i))
print(next(i))

# Output: 1 4 9
```

In the code above we are going to find the squares of the values between the provided range (start and stop). When we invoke the method iter(Squares(1, 3)) the \_\_iter\_\_ method is invoked which is a method that yields squares of the values between the provided range. In our example, we use the range from 1 to 3 so the output would be 1, 4, and 9 if we invoke the next() method.

https://www.analyticsvidhya.com/blog/2021/08/explore-the-magic-methods-in-python/#h-getitem-and-setitem-magic-method 

