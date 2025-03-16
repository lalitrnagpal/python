
# No need to declare a variable

a = 10              # binds a variable to a type

print(a)

del a               # unbinds the variable

try:
    print(a)
except Exception as ex:
    print('Exception occurred ', ex)

try:
    print(a)
except NameError as ne:
    print('Exception occurred ', ne.__class__)

