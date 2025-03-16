# Tuple

> Tuple objects are **immutable**: therefore, attempting to rebind or delete an item or slice of a tuple raises an exception. 

> Items of a tuple are arbitrary objects and may be of different types; tuple items may be mutable, but we recommend not mutating them

> **Slices of a tuple are also tuples**. Tuples have no normal (nonspecial) methods, except count and index, with the same meanings as for lists

> Tuples are similar to lists, but unlike lists, they **cannot be changed** after their creation (i.e., they are immutable).

> Main characteristics are being **ordered** , **heterogeneous** & **immutable**.

> Tuples are:
> **Ordered** - They maintain the order of elements.
> **Immutable** - They cannot be changed after creation.
> **Allow duplicates** - They can contain duplicate values.

> **Creating an empty Tuple**

```
tup = ()
print( tup )                                  # Output is ()
```

> **Using String**

```
tup = ( 'Geeks', 'For' )
print( tup )                                  # Output is ('Geeks', 'For')
```

> **Using List**

```
li = [ 1, 2, 4, 5, 6 ]
print( tuple( li ) )                            # Output is (1, 2, 4, 5, 6)
```

> **Using Built-in Function**

```
tup = tuple('Geeks')    
print(tup)                                  # Output is ('G', 'e', 'e', 'k', 's')
```

> **Creating a Tuple with Mixed Datatype**

```
tup = ( 5, 'Welcome', 7, 'Geeks' )
print( tup )                                  # Output is ( 5, 'Welcome', 7, 'Geeks' )
```

> **Iterate Through a Tuple**. We use the for loop to iterate over the items of a tuple. For example,

```
fruits = ( 'apple','banana','orange' )

for fruit in fruits:
    print( fruit )
```

> **Challenge**: Write a function to modify a tuple by adding an element at the end of it. For inputs with tuple (1, 2, 3) and element 4, the return value should be (1, 2, 3, 4). 
> Hint: You need to first convert the tuple to another data type, such as a list.

```
def modify_tuple(tupl, elem):
    l = list( tupl )                  # converting tuple to list
    l.append(elem)
    tup2 = tuple( l )                 # converting list to tuple
    print( tup2 )

modify_tuple( ( 1, 2, 3 ), 4 )

# Output is ( 1, 2, 3, 4 )
```

> **Creating a Tuple with nested tuples**

```
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)                                 # Output is ((0, 1, 2, 3), ('python', 'geek'))
```

> **Creating a Tuple with repetition**

```
tup1 = ('Geeks',) * 3
print(tup1)                                 # Output is ('Geeks', 'Geeks', 'Geeks')
```

> **Creating a Tuple with the use of loop**

```
tup = ('Geeks')
n = 5
for i in range( int(n) ):
    tup = ( tup, )
    print( tup )

# Output of above is
# ('Geeks',)
# (('Geeks',),)
# ((('Geeks',),),)
# (((('Geeks',),),),)
# ((((('Geeks',),),),),)
```

> **Accessing Tuple with Indexing**

```
tup = tuple( "Geeks" )
print( tup[0] )                               # Output is G
```

> **Accessing a range of elements using slicing**

```
print( tup[1:4] )                             # Output is ('e', 'e', 'k')
print( tup[:3] )                              # Output is ('G', 'e', 'e')
```

> **Tuple unpacking**

```
tup = ("Geeks", "For", "Geeks")
```

> This line unpack values of Tuple1

```
a, b, c = tup
print(a)                            # Output is Geeks
print(b)                            # Output is for
print(c)                            # Output is Geeks
```

```
y = (1, 2, 3)
print( type(y) )                      # output is <class 'tuple'>
print( type(y).__name__ )             # output is tuple
```

```
y = ( (1, 2,), (3, 4), (5, 6) )
print( type(y).__name__ )             # output is tuple
print( y[1] )                         # output is (3, 4) on index 1
print( type(y[1]).__name__ )          # output is tuple
```

```
# TypeError: 'tuple' object doesn't support item deletion
# del y[1]

# TypeError: 'tuple' object does not support item assignment
# y[1] = (7, 8)
```

> **Returns the number of times a specified value occurs in a tuple. Output is 1**

```
print( y.count((3,4)) )
```

> **Searches the tuple and returns  position of where it was found. Output is 1**

```
print( y.index( (3,4) ) )
```

> **Concatenation of Tuples**

```
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
```

```
tup3 = tup1 + tup2
print(tup3)
# Output is (0, 1, 2, 3, 'Geeks', 'For', 'Geeks')
```

> **Slicing of a Tuple with Numbers**

```
tup = tuple('GEEKSFORGEEKS')
```

> **Removing First element**

```
# Output is ('E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S')
print(tup[1:])
```

> **Reversing the Tuple**

```
# Output is ('S', 'K', 'E', 'E', 'G', 'R', 'O', 'F', 'S', 'K', 'E', 'E', 'G')
print(tup[::-1])
```

> **Printing elements of a Range**

```
# Output is ('S', 'F', 'O', 'R', 'G')
print(tup[4:9])
```

> **Deleting a Tuple**. Printing of Tuple after deletion results in an Error. 

```
tup = (0, 1, 2, 3, 4)
del tup
# Below print will result in error - name 'tup' is not defined. Did you mean: 'tup1'?
# print(tup)                        
```

> **Built-In Methods for Tuples**
```
tup = (0, 1, 2, 3, 4)
# Returns true if all element are true or if tuple is empty
print( tup.all() )
```

> **any** return true if any element of the tuple is true. if tuple is empty, return false

```
tup.any( (false, false, true, false ) )
```

> Returns **len** ( length ) of the tuple or size of the tuple

```
print( len(tup) )                           # Output - 5
```

> Returns **enumerate** object of tuple

```
print( enumerate(tup) )                     # Output - <enumerate object at 0x000001522D7E7560>
```

> return **max** element of given tuple

```
print( max(tup) )                           # Output - 4
```

> return **min** element of given tuple

```
print( min(tup) )                           # Output - 0
```

> **sum** up the numbers in the tuple

```
print( sum(tup) )                           # Output - 10
```

> input elements in the tuple and return a new **sorted** list

```
print( sorted( tup ) )                      # Output - [0, 1, 2, 3, 4]
```

> Convert an iterable to a **tuple**.

```
a = [1, 2, 3, 4, 5] # list

tup = tuple(a)
print('tuple:', tup)                        # tuple: (1, 2, 3, 4, 5)
```

> **Unpacking a tuple**. If we don’t need certain values, use _ as a throwaway variable or placeholder. Output 100 300

```
a, _, c = (100, 200, 300)
print(a)  
print(c)  
```

> **Using * for Variable-Length Unpacking**. Python allows catching multiple elements using *, known as the extended unpacking technique. Output is 1 and [2, 3, 4, 5]

```
a, *b = (1, 2, 3, 4, 5)
print(a)   
print(b)   
```

> **Unpacking Nested Tuples**. Tuples inside tuples can also be unpacked.

```
nested_tuple = (1, (2, 3), 4)
a, (b, c), d = nested_tuple

print(a)   # Output 1 
print(b)   # Output 2
print(c)   # Output 3
print(d)   # Output 4
```

> **Tuple Unpacking with * in Function Arguments**. Using *args: When defining a function, *args allows passing multiple arguments as a tuple

```
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4))      # Output is 10
```

> **Using * for Argument Unpacking**: Tuple unpacking can also be used when calling a function:

```
def add(a, b, c):
    return a + b + c

nums = (1, 2, 3)
print(add(*nums))  
```



