# List Comprehensions

> **List comprehensions** provide a **concise way to create lists**. <br>
Common applications are to make new lists where each element is the result of **some operations applied** <br>
**to each member of another sequence or iterable**, or to **create a subsequence** of those elements that <br>
satisfy a certain condition.<br>

> A simple example is creating a list of numbers from 0 to 9.

# Creates a list of numbers from 0 to 9
a = [i for i in range(10)]

print(a)

> **Using nested loops**

```
# Creates a list of tuples representing all combinations of (x, y)
# where both x and y range from 0 to 2.
coordinates = [(x, y) for x in range(3) for y in range(3)]

print(coordinates)

# Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

> **for loop vs. list comprehension**

```
squares = []

for x in range(10):
    squares.append(x**2)

squares
# Output is [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# We can calculate the list of squares without any side effects using:

squares = list( map( lambda x: x**2, range(10) ) )
```

> **or, equivalently:**

```
squares = [x**2 for x in range(10)]

# which is more concise and readable.
```

> **Conditional statements** in list comprehension

```
a = [1, 2, 3, 4, 5]

res = [val for val in a if val % 2 == 0]

print(res)

# Output: [2, 4]
```

> **Flattening a list of lists**

```
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

res = [val for row in mat for val in row]

print(res)

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

> **combine the elements of two lists** if they are not equal:

```
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# Output is [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

```

> and it’s equivalent to:

```
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs
# Output is [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

> Note how the order of the for and if statements is the same in both these snippets. If the expression is a tuple (e.g. the (x, y) in the previous example), it must be parenthesized.

```
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]
```

> **filter the list to exclude negative numbers**

```
[x for x in vec if x >= 0]
```

> apply a function to all the elements

```
[abs(x) for x in vec]
```

> **call a method on each element**

```
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
```

> **create a list of 2-tuples like (number, square)**

```
[(x, x**2) for x in range(6)]
```

> **the tuple must be parenthesized**, **otherwise** an **error** is raised

```
[x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
     ^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
```

> **flatten a list** using a listcomp with two 'for'

```
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

# print( [x, x**2 for x in range(6)] )         
```

> List comprehensions **can contain complex expressions and nested functions**:

```
from math import pi - imported above 

print( [str(round(pi, i)) for i in range(1, 6)] )
# Output is ['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

> **Nested List Comprehensions**. The initial expression in a list comprehension can be any arbitrary <br>
expression, including another list comprehension. Consider the following example of a 3x4 matrix <br> 
implemented as a list of 3 lists of length 4: <br>

```
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

> The following list comprehension will **transpose rows and columns**:

[[row[i] for row in matrix] for i in range(4)]

# Output is [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


# As we saw in the previous section, the inner list comprehension is evaluated in the context of the for that follows it, so this example is equivalent to:

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed

```

> which, in turn, is the same as:

```
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed
```

> In the real world, **you should prefer built-in functions** to complex flow statements. <br>
The **zip()** function would do a great job for this use case:

```
list(zip(*matrix))
```

```
list(range(3, 6))            # normal call with separate arguments

args = [3, 6]

list(range(*args))            # call with arguments unpacked from a list
```

> In the same fashion, **dictionaries** can deliver keyword arguments with the **\**-operator**:

```
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

parrot(**d)
```
