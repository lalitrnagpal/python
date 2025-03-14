x = 10

# Assigning to multiple variables
a = b = c = x
print(a, b, c, x)               # 10 10 10 10


# swapping variables
a = 10
b = 20

print(a, b)
a , b = b , a 
print(a, b)

# first, rest in the middle, last assignments
x = [1, 2, 3]
first, *second, third = x
print( first, second, third )                                 # 1 [2] 3
print( type(first), type(second), type(third) )               # <class 'int'> <class 'list'> <class 'int'>

## Same as below
first, middle, last = x[0], x[1: -1], x[-1]                   # 1 [2] 3
print(first, middle, last)






