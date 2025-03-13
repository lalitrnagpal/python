""" Just playing with some basic data types """

# Text Type:        str
# Numeric Types:    int, float, complex
# Sequence Types:   list, tuple, range
# Mapping Type:     dict
# Set Types:        set, frozenset
# Boolean Type:     bool
# Binary Types:     bytes, bytearray, memoryview
# None Type:        NoneType

i = 100
print(type(i))                                  # <class 'int'>

i1 = 100.21
print(type(i1))                                 # <class 'float'>

print(type(i1).__name__)                        # float

print(type(i1).__class__)                        # <class 'type'>

f = 12.123

print(type(f))                                  # <class 'float'>

s = 'c'
print(type(s))                                  # <class 'str'>

s1 = "hello"
print(type(s1))                                 # <class 'str'>

print(type(s1) is str)                          # True

# Use isinstance() rather than type() for a typecheck.Pylint warning!

print(isinstance(s1, str))                      # True

print(isinstance(i, (float, str, set, dict)))   # False

name = None                                     

print(type(name))                               # <class 'NoneType'>
print(type(name).__name__)                      # NoneType

name = Exception()

print(type(name))                               # <class 'Exception'>
print(type(name).__name__)                      # Exception

variable = "hello_world"
print(type(variable) is str)                    # True
print(isinstance(variable, str))                # True


L = [
    "Hello World",                              # <class 'str'>
    20,                                         # <class 'int'>
    20.5,                                       # <class 'float'>
    1j,                                         # <class 'complex'>
    ["apple", "banana", "cherry"],              # <class 'list'>
    ("apple", "banana", "cherry"),              # <class 'tuple'>
    range(6),                                   # <class 'range'>
    {"name" : "John", "age" : 36},              # <class 'dict'>
    {"apple", "banana", "cherry"},              # <class 'set'>
    frozenset({"apple", "banana", "cherry"}),   # <class 'frozenset'>
    True,                                       # <class 'bool'>
    b"Hello",                                   # <class 'bytes'>
    bytearray(5),                               # <class 'bytearray'>
    memoryview(bytes(5)),                       # <class 'memoryview'>
    None                                        # <class 'NoneType'>
]

for _ in range(len(L)):
    print(type(L[_]))


print('I\'m a Python fanatic')                  # You can escape a quote
print("I'm a Python fanatic")                   # This way may be more readable

print('A not very long string \
that spans two lines')

print('A not very long string\n\
that prints on two lines')

print("""An even bigger
string that spans
three lines""")                                 # Comments not allowed on previous lines

print(the_text = """\
First line
Second line                                     

""")                                            # Same as "First line\nSecond line\n" but more readable
                                                # Comments not allowed on previous lines


