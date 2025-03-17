# Closures

> A nested function that accesses values from local variables of “outer” (containing) functions is also known as a closure. 

```
def make_adder(augend):
   def add(addend):
      return addend + augend
   return add

add5 = make_adder(5)
add9 = make_adder(9)

print(add5(100)) 		# prints: 105
print(add9(100)) 		# prints: 109
```

> A def statement within a function body defines a nested function, and the function whose body includes the def is known as an outer function to the nested one. 

> Code in a nested function’s body may access (but not rebind) local variables of an outer function, also known as free variables of the nested function.

```
def percent1(a, b, c):
   def pc(x, total = a + b + c):
      return ( x * 100.0 ) / total
   print('Percentages are:', pc(a), pc(b), pc(c))

# Here’s the same functionality using nested scopes:

def percent2(a, b, c):
   def pc(x):
      return ( x * 100.0 ) / ( a + b + c)
   print('Percentages are:', pc(a), pc(b), pc(c))
```

Closures are sometimes an exception to the general rule that the object-oriented mechanisms covered in the next chapter are the best way to bundle together data and code. 

When you specifically need to construct callable objects, with some parameters fixed at object construction time, closures can be simpler and more direct than classes. 

An outer function that returns a closure is a “factory” for members of a family of functions distinguished by some parameters, such as the value of the argument augend in the previous example, which may often help you avoid code duplication.

The nonlocal keyword acts similarly to global, but it refers to a name in the namespace of some lexically surrounding function. When it occurs in a function definition nested several levels deep (a rarely needed structure!), the compiler searches the namespace of the most deeply nested containing function, then the function containing that one, and so on, until the name is found or there are no further containing functions, in which case the compiler raises an error (a global name, if any, does not match).

```
def make_counter():
   count = 0
   def counter():
      nonlocal count
      count += 1
      return count
   return counter

c1 = make_counter()
c2 = make_counter()

print(c1(), c1(), c1())         # prints: 1 2 3

print(c2(), c2())               # prints: 1 2

print(c1(), c2(), c1())         # prints: 4 3 5
```

