
### > Comparison Chaining

```
    a = 5
    b = 7
    c = 10
    d = 12
    x = a < b <= c < d                          # Will return True
    y = a < b and b <= c and c < d              # Will return True, same as above

    print(x)                                    # Above also applies short circuiting, left to right evaluation
    print(y)                                    # right evaluates only when left is true already

    # NESTED IF ELSE
    print("Both are equal" if a == b else "a is greater" if a > b else "b is greater")
```

### > Conditional Ternary Operator

```
    a = 10
    b = 20

    # python ternary operator
    min = "a is minimum" if a < b else "b is minimum"

    print(min)

```


### Asignment Expression - combine evaluation of an expression and the assignment of its result using the := operator
### := in an if/elif statement
### Code that assigns a value and then checks it can be collapsed using :=: 

```
input_string = "AA sdA";

re_match = re.match(r'Name: (\S)', input_string)
if re_match:
    print(re_match.groups(1))

# collapsed version using :=
if (re_match := re.match(r'Name: (\S)', input_string)):         # throws a error if not a string
    print(re_match.groups(1))
else:
    print('Not a String!', type(input_string).__name__)
```

#### Another Example
```
def get_next_value() -> str:                                    # dummy method
    return ''

def filter_condition(inputstr: str):                            # dummy method
    pass

current_value = get_next_value()

while current_value is not None:
    if not filter_condition(current_value):
        continue # BUG! Current_value is not advanced to next
        # ... do some work with current_value ...
    current_value = get_next_value()

# Instead of the above, we could do the following

while (current_value := get_next_value()) is not None:
    if not filter_condition(current_value):

```

### > Syntax for expressions

#### Dictionary Creation
``` 
    { key: expr, . . . } 
```

#### Set creation 
``` 
    { expr, ... } 
```

#### List creation 
``` 
    [ expr, ... ] 
```

#### Tuple creation (parentheses recommended, but not always required; at least one comma required), or just parentheses
``` 
    ( expr, ... ) 
```

#### Function call
``` 
    f ( expr, ... )
```

#### Slicing
``` 
    x [ index: index: step ]
```    

#### Indexing 
``` 
    x [ index ]
```    

#### Attribute reference 
``` 
    x . attr
```

#### Exponentiation (x to the yth power) 
``` 
    x ** y
```

#### Bitwise NOT, unary plus and minus
``` 
    ~ x, + x, - x
```

#### Multiplication, matrix multiplication, division, floor division, remainder
``` 
    x * y, x @ y, x / y, x // y, x % y
```

#### Addition, subtraction 
``` 
    x + y, x - y
```    

#### Left-shift, right-shift 
``` 
    x << y, x >> y
```

#### Bitwise AND 
``` 
    x & y 	
```

#### Bitwise XOR 
``` 
    x ^ y
```    

#### Bitwise OR 
``` 
    x | y
```    

#### Comparisons (less than, less than or equal, greater than, greater than or equal, inequality, equality)
``` 
    x < y, x <= y, x > y, x >= y, x != y, x == y
```

#### Identity tests 
``` 
    x is y, x is not y
```

#### Membership tests 
``` 
    x in y, x not in y
```

#### Boolean NOT 
``` 
    not x
```

#### Boolean AND 
``` 
    x and y 	
```

#### Boolean OR 
``` 
    x or y
```

#### Conditional expression (or ternary operator) 
``` 
    x if expr else y
```
