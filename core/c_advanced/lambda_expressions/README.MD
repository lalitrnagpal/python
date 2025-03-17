# Lambda Expressions

> ***Syntax***

```
lambda argument(s) : expression 
```

>Example:

```
greet_user = lambda name : print('Hey there,', name)
# Call the lambda
greet('Dolly')                     # Output- Hey there, Dolly
```



> An **anonymous function** means that a **function** is **without a name**. <br>
def keyword is used to define the normal functions and the **lambda keyword** is used <br>
to **create anonymous functions**.

> **List Comprehension is used to create lists**. <br>
**Lambda is function that can process** like other functions and thus return values or lists.

1. This function can have any number of arguments but only one expression, which is evaluated and returned.<br>
2. One is free to use lambda functions wherever function objects are required.<br>
3. You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.<br>
4. It has various uses in particular fields of programming, besides other types of expressions in functions.<br>

> Simple Examples

> Multiply two numbers
```
x = lambda a, b : a * b
print(x(5, 6))                      # Output 30
```

> Add 3 numbers

```
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))                   # Output 13
```

> The power of lambda is better shown when you use them as an anonymous function inside another function.<br>
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

```
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))                # Output 22
```

> Use lambda functions when an anonymous function is required for a short period of time.



> list from range 0 to 10

```
list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_)
```

> A lambda function to filter out **even numbers from a list**

```
my_list = [1, 2, 3, 4, 5]

new_list = list( filter( lambda x: x % 2 != 0, my_list ) )

print( new_list )
```

> **Simple Examples**

```
filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Geeks101"))
# Output: filter_nums(): Geeks
```

> **A cube lambda example**

```
cubo = lambda num:num ** 3
[cubo(x) for x in range(10)]

#Output: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```

> **Just adding a exclamation mark to a sentence**

```
do_exclaim = lambda s: s + '!'
print("do_exclaim():", do_exclaim("I am tired"))
# Output: do_exclaim(): I am tired!
```

> **lambda function gets more helpful when used inside a function**<br>
We can use lambda function inside **map()**, **filter()**, **sorted()** and many other functions. 

```
l = ["1", "2", "9", "0", "-1", "-2"]
print("Sorted numerically:", sorted(l, key=lambda x: int(x)))

#Output: Sorted numerically: ['-2', '-1', '0', '1', '2', '9']
```

> Add 10 to each str in the list. Added 10 to each item after type and # casting to int, <br>
then convert items to string again

```
l = ["1", "2", "9", "0", "-1", "-2"]
print("Operation on each item using lambda and map()", list(map(lambda x: str(int(x) + 10), l)))

# Output: Operation on each item using lambda and map() ['11', '12', '19', '10', '9', '8']
```

> **Sum of all digits in a str**
> str is a sequence of characters. Typecastes n to str, iterates on characters in it <br>
and type castes to int, all come under a list due to [] which is passed to sum function <br>

```
find_sum = lambda n: sum([int(x) for x in str(n)])

print("find_sum():", find_sum(101))

# Output: find_sum(): 2
```

> **lambda function**
> **Map basically iterates every element in the list_ and returns the lambda function result**<br>

```
lambda_list = list( map( lambda x: x * 2, list_) )

print(lambda_list)

# Output:
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

> **list comprehension**

```
list_comp = [x * 2 for x in list_]

print(list_comp)

# Output:
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

```







