# Dictionary

> Python provides a variety of operations applicable to dictionaries. Since dictionaries <br>
are containers, the built-in len function can take a dictionary as its argument and return the <br>
number of items (key/value pairs) in the dictionary

> The k in D operator checks whether the object k is a key in the dictionary D

> k not in D is like not (k in D).

> Dictionary keys must be immutable, such as tuples, strings, integers, etc. We cannot use mutable (changeable) objects such as lists as keys.

> Keys of a dictionary must be unique



> **Creating a Dictionary**

```
d = {'x':42, 'h':3.14, 'z':7}
```

> **Adding a item** to a dictionary

```
country_capitals["Italy"] = "Rome"
```

> **Remove dictionary item**

```
del country_capitals["Germany"]
```

> **Change dictionary item**

```
country_capitals["Italy"] = "Rome"
```

> **Iterate through a dictionary**

```
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" 
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)                              # Output as United States   Italy

print()

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]         # Output as Washington D.C. Rome
    print(capital)
```

> **Dictionary Length**

```
country_capitals = {"England": "London", "Italy": "Rome"}
print(len(country_capitals))                                    # Output: 2
```

> **Membership Test**

```
file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

# use of in and not in operators
print(".pdf" in file_types)       # Output: True
print(".mp3" in file_types)       # Output: False
print(".mp3" not in file_types)   # Output: True
```

> **Merge two dictionaries**

```
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d1.update(d2)
print(d1)                       # Output: {'x': 1, 'y': 3, 'z': 4}
```

> **Merge using the | operator**

```
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = d1 | d2
print(d3)                       # Output {'x': 1, 'y': 3, 'z': 4}
```

> **Accessing elements by key**

```
d['x'] 					# 42
d['z'] 					# 7
d['a'] 					# raises KeyError exception
```

> **Assigning a value using the key**

```
d['a'] = 16             # d is now {'x':42, 'h':3.14, 'a':16}
```

> **Creating Dictionaries**

```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```

```
Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
```

```
print( len(thisdict) )
```

> **dict() constructor**

```
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
```

> **Sorting the dictionary**

```
from collections import OrderedDict

d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
```

> **sorted by key**

```
OrderedDict(sorted(d.items(), key-lambda t: t[0]))

# Output: OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
```

> **sorted by value**

```
OrderedDict(sorted(d.items(), key-lambda t: t[1]))

# Output: OrderedDict([('pear', 1), ('orange', 2), ('banana", 3), ('apple', 4)])
```

> **dictionary sorted by length of the key string**

```
OrderedDict(sorted(d.items(), key-lambda t: len(t[0]))) OrderedDict([('pear', 1), ('apple', 4), ('banana', 3), ('orange', 2)])

```

> The items, keys, and values methods return values known as view objects. If the underlying dict changes, <br>
the retrieved view also changes; Python doesn’t allow you to alter the set of keys in the underlying dict <br>
while using a for loop on any of its view objects

> **fromKeys() method**
> Dictionaries also support the class method fromkeys(seq, value), which returns  a dictionary containing all the keys of the given iterable seq

```
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)                             # Output: {'key1': 0, 'key2': 0, 'key3': 0}
```

> Never Modify a dict’s Keys While Iterating on It <br>
Don’t ever modify the set of keys in a dict (i.e., add or remove keys) while iterating over that dict or any of the iterable views returned by its methods

> **Non Mutating Methods**

```
d1 = d.copy()           # Returns a shallow copy of the dictionary
print(d1)
```

```
d.get(k[, x])           # Returns d[k] when k is a key in d; otherwise, returns x
```

```
d.items()               # dict_items([('x', 42), ('h', 3.14), ('z', 7)])       
```

```
d.keys()                # dict_keys(['x', 'h', 'z'])
```

```
d.values()              # dict_values([42, 3.14, 7])
```

```
d.clear()               # Removes all items from d, leaving d empty
```

```
d.pop(k[, x])           # Removes and returns d[k] when k is a key in d; otherwise, returns x
```

```
d.popitem()             # Removes and returns the items from d in last-in, first-out order set
```

```
d.setdefault(k, x)      # Returns d[k] when k is a key in d; otherwise, sets d[k] equal to x
```

```
d.update(d1)            # For each k in mapping d1, sets d[k] equal to d1[k]
```

> pop method returns the same result as get, but when k is a key in D, pop also has the side effect of removing D[k] 

> update method (but not the | and |= operators) can also accept an iterable of key/value pairs as an alternative argument 

> The return values of the items and keys methods also implement set nonmutating methods and behave much like frozensets

> The popitem method can be unsed for destructive iteration on a dictionary. Both items and popitem return dictionary items as key/value pairs. 

> popitem is usable for a loop on a huge dictionary, when what you want is to “consume” the dictionary in the course of the loop.

> **Dictionary Unpacking**

```
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = {**d1, **d2}
print(d3)                               # Output: {'x': 1, 'y': 3, 'z': 4}

# **d1 and **d2 unpack the key-value pairs of d1 and d2 into the new dictionary d3.
# Keys from d2 overwrite duplicates from d1.

```

> **Using a loop**

```
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = d1.copy()

for key, value in d2.items():
    d3[key] = value

print(d3)                               # Output: {'x': 1, 'y': 3, 'z': 4}
```

> **Convert key-values list to flat dictionary** using the **dict()** constructor

```
a = [("name", "Alice"), ("age", 25), ("city", "New York")]          # List of key-value pairs as tuples

# Convert the list of key-value pairs into a flat dictionary using the dict() constructor
res = dict(a)

print(res)  

```

> **Using Dictionary Comprehension**

```
a = [("name", "Alice"), ("age", 25), ("city", "New York")]  # List of key-value pairs as tuples

# Use dictionary comprehension to create a dictionary by unpacking each tuple into key and value
res = {key: value for key, value in a}

print(res)

# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Dictionary comprehension iterates over the list a, unpacking each tuple into key and value.
# Each key is mapped to its corresponding value, and the comprehension directly constructs the dictionary res.
```

> **Using zip() function**

```
a = ["name", "age", "city"]  # List of keys
b = ["Alice", 25, "New York"]  # List of values

# Use zip to pair each key from 'a' with the corresponding value from 'b', then convert the pairs to a dictionary
res = dict( zip(a, b) )

print(res) 

# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
# zip() function combines elements from the lists a (keys) and b (values) into key-value pairs.
# dict() constructor then converts the paired elements into a dictionary, mapping each key to its corresponding value.
```