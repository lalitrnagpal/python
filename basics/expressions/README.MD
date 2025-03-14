
> Syntax for expressions

### Dictionary Creation
``` 
    { key: expr, . . . } 
```

### Set creation 
``` 
    { expr, ... } 
```

### List creation 
``` 
    [ expr, ... ] 
```

### Tuple creation (parentheses recommended, but not always required; at least one comma required), or just parentheses
``` 
    ( expr, ... ) 
```

### Function call
``` 
    f ( expr, ... )
```

### Slicing
``` 
    x [ index: index: step ]
```    

### Indexing 
``` 
    x [ index ]
```    

### Attribute reference 
``` 
    x . attr
```

### Exponentiation (x to the yth power) 
``` 
    x ** y
```

### Bitwise NOT, unary plus and minus
``` 
    ~ x, + x, - x
```

### Multiplication, matrix multiplication, division, floor division, remainder
``` 
    x * y, x @ y, x / y, x // y, x % y
```

### Addition, subtraction 
``` 
    x + y, x - y
```    

### Left-shift, right-shift 
``` 
    x << y, x >> y
```

### Bitwise AND 
``` 
    x & y 	
```

### Bitwise XOR 
``` 
    x ^ y
```    

### Bitwise OR 
``` 
    x | y
```    

### Comparisons (less than, less than or equal, greater than, greater than or equal, inequality, equality)
``` 
    x < y, x <= y, x > y, x >= y, x != y, x == y
```

### Identity tests 
``` 
    x is y, x is not y
```

### Membership tests 
``` 
    x in y, x not in y
```

### Boolean NOT 
``` 
    not x
```

### Boolean AND 
``` 
    x and y 	
```

### Boolean OR 
``` 
    x or y
```

### Conditional expression (or ternary operator) 
``` 
    x if expr else y
```
