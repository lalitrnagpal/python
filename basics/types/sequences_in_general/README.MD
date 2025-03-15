> A List Example

```
l = [1, 2, 3, 6, 5, 4]
```

```
print( min(l) )
```

```
print( max(l) )
```

```
print ( len(l) )
```

```
print( sum(l) )
```

> Concatenation / Multiplication is possible on Sequences
```
a = [3, 2, 1]

a += a

print(a)                # Output is [3, 2, 1, 3, 2, 1]

a += 2

print(a)                # will result in error, int is not iterable

a *= 3

print(a)                # Output is [ 3, 2, 1, 3, 2, 1, 3, 2, 1 ]

a *= 0 

print(a)                # Output is []
```

> Membership testing

```
x = 1
y = 9

l = [ 3, 2, 4, 1 ]

print( x in l )         # Output is True
print( y not in l )     # Output is True

```

> Indexing a Sequence

x = [10, 20, 30, 40]

print( x[1] )                    # Output is 20

print( x[-1] )                   # Output is 40

print( x[-3] )                   # Ouput is 20

print( x[-4] )                   # Output is 10

print( x[-4: ] )                 # Output is 10, 20, 30, 40

> creating a list with a range

y = list(range(10)) 	        # values from 0-9

y[-5:] 			                # last five items
[5, 6, 7, 8, 9]

y[::2] 			                # every other item – step 2
[0, 2, 4, 6, 8]

y[10:0:-2] 		                # every other item, in reverse order
[9, 7, 5, 3, 1]

y[:0:-2] 			            # every other item, in reverse order (simpler)
[9, 7, 5, 3, 1]

y[::-2] 			            # every other item, in reverse order (best)
[9, 7, 5, 3, 1]

> 