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
```

You can pass named arguments for readability purposes whenever you think that identifying the role of each argument and controlling the order of arguments enhances your code’s clarity

```
def f(middle, begin='init', end='finis'):
   return begin+middle+end

print(f('tini', end='')) 		# prints: inittini

print(f('tini', end='ooo')) 	# prints: inittiniooo
```

With the named argument end='', the caller specifies a value (the empty string '') for f’s third parameter, end, and still lets f’s second parameter, begin, use its default value, the string 'init'. You may pass the arguments as positional even when parameters are named; for example, with the preceding function:

```
print(f('a','c','t')) 	                    # prints: cat

print(divide(dividend=94, divisor=12))      # prints: 7

print(divide(divisor=12))                   # prints: 7

```

> At the end of the arguments in a function call, you may optionally use either or both of the special forms *seq and **dct. 

> If both forms are present, the form with two asterisks must be last. 

> \*seq passes the items of iterable seq to the function as positional arguments (after the normal positional arguments, if any, that the call gives with the usual syntax). seq may be any iterable. 

> \*\*dct passes the items of dct to the function as named arguments, where dct must be a mapping whose keys are all strings. Each item’s key is a parameter name, and the item’s value is the argument’s value.

> You may want to pass an argument of the form *seq or **dct when the parameters use similar forms. You may want to print the sum of all the values in the dictionary d. This is easy with *seq:

```
def sum_sequence(*numbers):
   return sum(numbers)

d = {'a': 1, 'b': 100, 'c': 1000}
print(sum_sequence(*d.values()))

# Output: 1101
```

> You may even pass *seq or **dct when calling a function that does not use the corresponding form in its signature. In that case, you must ensure that the iterable seq has the right number of items, or that the dictionary dct uses the right identifier strings as keys; otherwise, the call raises an exception. 

> **"Keyword-only" parameters**

**Parameters after a positional argument collector** in the function’s signature are known as **keyword-only parameters**: the corresponding arguments, if any, must be named arguments. 

Keyword-only parameters can be either **positional** or **named**. 

**Functions requiring keyword-only parameter** specifications without collecting "surplus" positional arguments indicate the start of the keyword-only parameter specifications with a dummy parameter **consisting solely of an asterisk (\*)**

```
def f(a, *, b, c=56):                           # b and c are keyword only
   return a, b, c

f(12, b=34) 		                            # Returns (12, 34, 56) c is optional, it has a default

f(12) 			                                # Raises a 'TypeError' exception, since you didn't pass b

# Error message is: missing 1 required keyword-only argument: 'b'
```

**If you also specify the special form \*\*kwds**, it **must come at the end** of the parameter list (after the keyword-only parameter specifications, if any). For example:

```
def g(x, *a, b=23, **k): 			            # b is keyword only
   return x, a, b, k

g(1, 2, 3, c=99) 				                # Returns (1, (2, 3), 23, {'c': 99})
```

> [!NOTE] [!IMPORTANT]

<details open>
---

1. Arguments of the form **\*expression** are internally **replaced by a sequence of positional arguments** obtained by **iterating over expression**.

2. Arguments of the form **\*\*expression** are internally **replaced by a sequence of keyword arguments** whose names and values are **obtained by iterating over expression’s items()**.

3. Say that the function has **N positional parameters** and the **call has M positional arguments**:

   1. When **M ≤ N**, bind all the **positional arguments to the first M positional parameter** names; the **remaining positional parameters, if any, must be matched by named arguments**.

   2. When **M > N**, bind the **remaining positional arguments to named parameters in the order in which they appear in the signature**. This process terminates in one of three ways:

       1. All positional arguments have been bound.

       2. The next item in the signature is a \* argument collector: the interpreter raises a TypeError exception.

       3. The next item in the signature is a \*name argument collector: the remaining positional arguments are collected in a tuple that is then bound to name in the function call namespace.

4. The **named arguments are then matched, in the order of the arguments’ occurrences in the call**, by name with the parameters—both positional and named.

    Attempts to rebind an already bound parameter name raise a TypeError exception.

5. If **unmatched named arguments remain at this stage**:

    1. When the **function signature includes a \*\*name collector, the interpreter creates a dictionary with key/value pairs (argument's_name, argument's_value), and binds it to name in the function call namespace**.

    2. In the absence of such an argument collector, Python raises a **TypeError exception**.

6. Any **remaining unmatched named parameters are bound to their default values**.

---
</details>

> **Argument Passing**

All argument passing in Python is by value 

Passing a mutable object as an argument, however, allows the function to make changes to that object, because Python passes a reference to the object itself, not a copy. Rebinding a variable and mutating an object are totally disjoint concepts

```
def f(x, y):
   x = 23
   y.append(42)

a = 77
b = [99]

f(a, b)
print(a, b) 	# prints: 77 [99, 42]
```

> **Namespace**

> Local Variables

A function’s parameters, plus any names that are bound (by assignment or by other binding statements, such as def) in the function body, make up the function’s local namespace, also known as its local scope. Each of these variables is known as a  local variable of the function

Variables that are not local are known as global variables 

Whenever a function’s local variable has the same name as a global variable, that name, within the function body, refers to the local variable, not the global one. 

> Global Variables/ Global statement

where identifiers is one or more identifiers separated by commas (,). The identifiers listed in a global statement refer to the global variables (i.e., attributes of the module object) that the function needs to bind or rebind. For example, the function counter could be implemented using **global** and a **global** variable, rather than an attribute of the function object:

```
_count = 0

def counter():
   global _count
   _count += 1
   return _count
```

Without the global statement, the counter function would raise an UnboundLocalError exception when called, because _count would then be an uninitialized (unbound) local variable. 

While the global statement enables this kind of programming, this style is inelegant and ill-advised.

> Nested Functions

A def statement within a function body defines a nested function, and the function whose body includes the def is known as an outer function to the nested one. 

Code in a nested function’s body may access (but not rebind) local variables of an outer function, also known as free variables of the nested function.

```
def percent1(a, b, c):
   def pc(x, total = a + b + c):
      return ( x * 100.0 ) / total
   print('Percentages are:', pc(a), pc(b), pc(c))

Here’s the same functionality using nested scopes:

def percent2(a, b, c):
   def pc(x):
      return ( x * 100.0 ) / ( a + b + c)
   print('Percentages are:', pc(a), pc(b), pc(c))
```




