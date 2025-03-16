# Dictionary

> Python provides a variety of operations applicable to dictionaries. Since dictionaries <br>
are containers, the built-in len function can take a dictionary as its argument and return the <br>
number of items (key/value pairs) in the dictionary

> The k in D operator checks whether the object k is a key in the dictionary D
> k not in D is like not (k in D).

> Creating a Dictionary

```
d = {'x':42, 'h':3.14, 'z':7}
```

> Accessing elements by key

```
d['x'] 					# 42
d['z'] 					# 7
d['a'] 					# raises KeyError exception
```

> Assigning a value using the key

```
d['a'] = 16             # d is now {'x':42, 'h':3.14, 'a':16}
```

> Creating Dictionaries

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

# sorted by key

OrderedDict(sorted(d.items(), key-lambda t: t[0]))

# Output: OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# sorted by value

OrderedDict(sorted(d.items(), key-lambda t: t[1]))

# Output: OrderedDict([('pear', 1), ('orange', 2), ('banana", 3), ('apple', 4)])

# dictionary sorted by length of the key string

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

