# List Comprehensions

from math import pi

squares = []

for x in range(10):
    squares.append(x**2)

print( squares )
# Output is [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = list(map(lambda x: x**2, range(10)))
print( squares )
# Output is [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


squares = [x**2 for x in range(10)]
print( squares )
# Output - [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print( [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] )
# Output is [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print( combs )
# Output is [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

vec = [-4, -2, 0, 2, 4]
print( [x*2 for x in vec] )
# Output is [-8, -4, 0, 4, 8]

print( [x for x in vec if x >= 0] )
# Output is [0, 2, 4]

print( [abs(x) for x in vec] )
# Output is [4, 2, 0, 2, 4]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print( [weapon.strip() for weapon in freshfruit] )
# Output is ['banana', 'loganberry', 'passion fruit']

print( [(x, x**2) for x in range(6)] )
# Output is [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

vec = [[1,2,3], [4,5,6], [7,8,9]]
print( [num for elem in vec for num in elem] )
# Output is [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print( [x, x**2 for x in range(6)] )

# List comprehensions can contain complex expressions and nested functions:
# from math import pi - imported above 

print( [str(round(pi, i)) for i in range(1, 6)] )
# Output is ['3.1', '3.14', '3.142', '3.1416', '3.14159']

# Nested List Comprehensions. 
# The initial expression in a list comprehension can be any arbitrary 
# expression, including another list comprehension. Consider the following example of a 3x4 matrix <br> 
# implemented as a list of 3 lists of length 4: <br>

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# The following list comprehension will transpose rows and columns:

print( [[row[i] for row in matrix] for i in range(4)] )

# Output is [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


# As we saw in the previous section, the inner list comprehension is evaluated in the context of the for that follows it, so this example is equivalent to:

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print( transposed )

# which, in turn, is the same as:

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print( transposed )

# In the real world, you should prefer built-in functions to complex flow statements. The zip() function would do a great job for this use case:


list(zip(*matrix))

list(range(3, 6))            # normal call with separate arguments

args = [3, 6]

list(range(*args))            # call with arguments unpacked from a list

# In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

parrot(**d)         # Output: -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

