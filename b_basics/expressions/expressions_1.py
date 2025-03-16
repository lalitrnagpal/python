
### > Comparison Chaining

import re


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

### > Conditional Ternary Operator


a = 10
b = 20

# python ternary operator

min = "a is minimum" if a < b else "b is minimum"

print(min)

# Comparison Chaining

a = 5
b = 7
c = 10
d = 12
x = a < b <= c < d                                 # True
y = a < b and b <= c and c < d                     # Same as above, True
    
print(x)                                            
print(y)                                            

# Asignment Expression - combine evaluation of an expression and the assignment of its result using the := operator
# := in an if/elif statement
# Code that assigns a value and then checks it can be collapsed using :=: 

input_string = "AA sdA";

re_match = re.match(r'Name: (\S)', input_string)
if re_match:
    print(re_match.groups(1))

# collapsed version using :=
if (re_match := re.match(r'Name: (\S)', input_string)):         # throws a error if not a string
    print(re_match.groups(1))
else:
    print('Not a String!', type(input_string).__name__)

# Another Example
def get_next_value() -> str:                           # dummy method
    return ''

def filter_condition(inputstr: str):            # dummy method
    pass

current_value = get_next_value()

while current_value is not None:
    if not filter_condition(current_value):
        continue # BUG! Current_value is not advanced to next
        # ... do some work with current_value ...
    current_value = get_next_value()

while (current_value := get_next_value()) is not None:
    if not filter_condition(current_value):
        continue # no bug, current_value advances in while statement

# ... do some work with current_value ...


# { key: expr, . . . }                              Dictionary Creation
# { expr, ... } 	                                Set creation 
# [ expr, ... ] 	                                List creation 
# ( expr, ... ) 	                                Tuple creation (parentheses recommended, but not always required; at least one comma required), or just parentheses
# f ( expr, ... ) 	                                Function call 
# x [ index: index: step ] 	                        Slicing 
# x [ index ] 	                                    Indexing 
# x . attr 	                                        Attribute reference 
# x ** y 	                                        Exponentiation (x to the yth power) 
# ~ x, + x, - x 	                                Bitwise NOT, unary plus and minus 
# x * y, x @ y, x / y, x // y, x % y	            Multiplication, matrix multiplication, division, floor division, remainder
# x + y, x - y 	                                    Addition, subtraction 
# x << y, x >> y 	                                Left-shift, right-shift 
# x & y 	                                        Bitwise AND 
# x ^ y 	                                        Bitwise XOR 
# x | y 	                                        Bitwise OR 
# x < y, x <= y, x > y, x >= y, x != y, x == y	    Comparisons (less than, less than or equal, greater than, greater than or equal, inequality, equality)
# x is y, x is not y 	                            Identity tests 
# x in y, x not in y 	                            Membership tests 
# not x 	                                        Boolean NOT 
# x and y 	                                        Boolean AND 
# x or y 	                                        Boolean OR 
# x if expr else y 	                                Conditional expression (or ternary operator) 

