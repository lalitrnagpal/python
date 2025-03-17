# Functions

> A function is a group of statements that execute upon request. There are no disadvantages: clarity, readability and code reusability all improve when you avoid having any substantial chunks of module-level code

> Code in a function body may be faster than at a module’s top level

> Python is somewhat unusual in the flexibility it affords the programmer in defining and calling functions

> You can pass a function as an argument in a call to another function, and a function can return another function as the result of a call. 

> Functions can also be keys in a dictionary. The fact that functions are ordinary objects in Python is often expressed by saying that functions are first-class objects

> The def statement is the usual way to create a function. def is a single-clause compound statement with the following syntax:

```
def function_name( parameters ):
   statement(s)

# Example

def twice(x):
   return x*2
```

> **Parameters**
>
> **Mutable default parameter values**
 
When a named parameter’s default value is a mutable object, and the function body alters the parameter, things get tricky

```
def f(x, y=[]):
   y.append(x)
   return id(y), y

print(f(23)) # prints: (4302354376, [23])

print(f(42)) # prints: (4302354376, [23, 42])
```

If you want y to be a new, empty list object, each time you call f with a single argument (a far more frequent need!), use the following idiom instead:

```
def f(x, y=None):
  if y is None:
     y = []
     y.append(x)
     return id(y), y

print(f(23)) 	# prints: (4302354376, [23])
print(f(42)) 	# prints: (4302180040, [42])
```

There may be cases in which you explicitly want a mutable default parameter value that is preserved across multiple function calls, most often for caching purposes, as in the following example:

``` 
def cached_compute(x, _cache={}):
   if x not in _cache:
      _cache[x] = costly_computation(x)
   return _cache[x]
```

Such caching behavior (also known as memoization) is usually best obtained by decorating the underlying costly_computation function with functools.lru_cache


> **Argument Collector Parameter**

The presence of argument collectors (**the special forms \*, \*name, or \*\*name**) in a function’s signature allows a function **to prohibit (\*)** or **collect positional (*name)** or **named (\*\*name) arguments** that do not match any parameters

There is **no requirement to use specific names**—you can use any identifier you want in each special form. \*args and \*\*kwds or \*\*kwargs, as well as \*a and \*\*k, are popular choices

> **\* form**

Here’s a function that accepts any number of positional arguments **\*numbers** and returns their sum 
```
 def sum_sequence(*numbers):
   return sum(numbers)

 print(sum_sequence(23, 42))                  # prints: 65
 ```

> **\*\* form**

Similarly, **\*\*kwds** specifies that any extra named arguments (i.e., those named arguments not explicitly specified in the signature) get collected into a (possibly empty) dictionary whose items are the names and values of those arguments, bound to the name kwds in the function call namespace. 

```
def inc_dict(d, **values):
  for key, value in values.items():
     if key in d:
         d[key] += value
      else:
         d[key] = value
my_dict = {'one': 1, 'two': 2}

inc_dict(my_dict, one=3, new=42)
 
print(my_dict)          # prints: {'one': 4, 'two': 2, 'new':42}
```

Without a named argument collector, unmatched named arguments raise a **Type Error exception**

> **Attributes of Function Objects**

The def statement sets some attributes of a function object f. The string attribute **f.__name__** is the identifier that def uses as the function’s name. You may rebind __name__ to any string value, but trying to unbind it raises a **TypeError** exception. **f.__defaults__**, which you may freely rebind or unbind, is the tuple of default values for named parameters 
 
> **Docstrings**

You may use or rebind a function f’s docstring attribute as **f.__doc__**

```
def sum_sequence(*numbers):
   """Return the sum of multiple numerical arguments.
   The arguments are zero or more numbers.
   The result is their sum.
   """
   return sum(numbers)
```

> **Function Annotations**

You can also annotate the return value of the function

```
def f(a:'foo', b)->'bar': 
    pass

f.__annotations__

# Output would be {'a': 'foo', 'return': 'bar'}

```

As shown in this example, the __annotations__ attribute of the function object is a dict mapping each annotated identifier to the respective annotation.

> **Return Statements**

Use the return keyword in Python only inside a function body, optionally follow it with an expression. When return executes, the function terminates, and the value of the expression is the function’s result. 

A function returns None when it terminates by reaching the end of its body, or by executing a return statement with no expression 

> **Positional and Named Arguments**

- It is a syntax error for named arguments to precede positional ones in a function call. 

- Zero or more positional arguments may be followed by zero or more named arguments. 

- Each positional argument supplies the value for the parameter that corresponds to it by position (order) in the function definition. 

- There is no requirement for positional arguments to match positional parameters, or vice versa—if there are more positional arguments than positional parameters, the additional

- In the absence of any named argument collector (\*\*name) parameter, each argument’s name must be one of the parameter names used in the function’s signature

```
def f(a, b, c=23, d=42, *x):
   print(a, b, c, d, x)

f(1,2,3,4,5,6)                  # prints: 1 2 3 4 (5, 6)
```

```
def f(a, b, *x, c=23, d=42):
   print(a, b, x, c, d)

f(1,2,3,4,5,6) 				    # prints: 1 2 (3, 4, 5, 6) 23 42

```

A function call must supply, via a positional or a named argument, exactly one value for each mandatory parameter, and zero or one value for each optional parameter

```
def divide(divisor, dividend=94):
   return dividend // divisor

print(divide(12))                           # prints: 7

print(divide(12, 94))                       # prints: 7

print(divide(dividend=94, divisor=12))      # prints: 7

print(divide(divisor=12))                   # prints: 7

```










