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
> 
> When a named parameter’s default value is a mutable object, and the function body alters the parameter, things get tricky
>
> ```
> def f(x, y=[]):
>    y.append(x)
   > return id(y), y
>
> print(f(23)) # prints: (4302354376, [23])
> 
> print(f(42)) # prints: (4302354376, [23, 42])
> ```
>
> If you want y to be a new, empty list object, each time you call f with a single argument (a far more frequent need!), use the following idiom instead:
>
> ```
> def f(x, y=None):
>   if y is None:
>      y = []
>      y.append(x)
>      return id(y), y
>
> print(f(23)) 	# prints: (4302354376, [23])
>
> print(f(42)) 	# prints: (4302180040, [42])
> ```

> There may be cases in which you explicitly want a mutable default parameter value that is preserved across multiple function calls, most often for caching purposes, as in the following example:
>
> ``` 
> def cached_compute(x, _cache={}):
>    if x not in _cache:
>       _cache[x] = costly_computation(x)
>    return _cache[x]
> ```
>
> Such caching behavior (also known as memoization) is usually best obtained by decorating the underlying costly_computation function with functools.lru_cache
>

> **Argument Collector Parameter**
>
> The presence of argument collectors (**the special forms \*, \*name, or \*\*name**) in a function’s signature allows a function **to prohibit (\*)** or **collect positional (*name)** or **named (\*\*name) arguments** that do not match any parameters
>
> There is **no requirement to use specific names**—you can use any identifier you want in each special form. \*args and \*\*kwds or \*\*kwargs, as well as \*a and \*\*k, are popular choices
>
> Here’s a function that accepts any number of positional arguments **\*numbers**and returns their sum 
> ```
> def sum_sequence(*numbers):
>   return sum(numbers)
>
> print(sum_sequence(23, 42))                  # prints: 65
> ```
>
> Similarly, **\*\*kwds** specifies that any extra named arguments (i.e., those named arguments not explicitly specified in the signature) get collected into a (possibly empty) dictionary whose items are the names and values of those arguments, bound to the name kwds in the function call namespace. 
>
> ```
> def inc_dict(d, **values):
>   for key, value in values.items():
>      if key in d:
>         d[key] += value
>      else:
>         d[key] = value
> my_dict = {'one': 1, 'two': 2}
>
> inc_dict(my_dict, one=3, new=42)
> 
> print(my_dict)          # prints: {'one': 4, 'two': 2, 'new':42}
> ```
>









