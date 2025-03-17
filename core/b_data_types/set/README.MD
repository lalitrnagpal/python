# set 

> set is **a container**. <br> 
A **set is iterable**, so you can pass it to any function or method that takes an iterable argument<br>

## Methods

```
s = { 'a', 'c', 'e', 'b', 'd' }
s1 = {'b', 'e', 'd'}
s3 = {'z', 'y', 'x'}
```

> **.copy()** method

```
s_copy = s.copy()
print(s_copy)                           # Output {'d', 'a', 'b', 'e', 'c'}
```

> **.difference()** method

```
print( s.difference(s1) )               # Output {'a', 'c'}
```

> **.intersection()** method

```
print( s.intersection(s1) )             # Output {'b', 'e', 'd'}
```

> **.isdisjoint()** method

```
print( s.isdisjoint(s1) )               # Output False
```

> **.issubset()** method

```
print( s1.issubset(s) )                 # Output True
```

> **.issuperset()** method

```
print( s.issuperset(s1) )               # Output True
```

> **.symmetric_difference()** method

```
s.symmetric_difference(s1)              
```

> **.union()** method

```
s.union(s1)                             # Output {'a', 'c', 'd', 'b', 'e'}
```

> **.add()** method

```
x = 'r'
s.add(x)
print(s)                                # Output {'e', 'c', 'b', 'r', 'd', 'a'}                   
```

> **.clear()** method

```
s.clear()
print(s)                                # Output set()
```

```
s = { 'a', 'c', 'e', 'b', 'd' }
s1 = {'b', 'e', 'd'}
s3 = {'z', 'y', 'x'}
```

> **.discard()** method

```
x = 'r'
s.discard(x)
print(s)                                    # Output {'e', 'c', 'b', 'd', 'a'}
```

> **.pop()** method

```
print( s.pop() )                            # Output 'e'
```

> **.remove()** method

```
# s.remove(x)                               # KeyError: 'r' - there is no 'r'

s.add(x)
s.remove(x)                                 # can remove now
print(s)                                    # Output is {'c', 'b', 'd', 'a'}
```

> **pop()** method can be used for destructive iteration on a set

```
while S:
   item = S.pop()
print(s)
# Output set()
```

> 
