#  A List Example

l = [1, 2, 3, 6, 5, 4]

print( min(l) )

print( max(l) )

a = [3, 2, 1]

a += a

print(a)                # Outpus is [3, 2, 1, 3, 2, 1]

# a += 2                # will result in Error
# print(a)              # Error - int object is not iterable

a *= 3

print(a)                # Output is [ 3, 2, 1, 3, 2, 1, 3, 2, 1 ]

a *= 0

print(a)                # []

# Membership testing

x = 1
y = 9
l = [ 3, 2, 4, 1 ]

print( x in l )         # True

print( y not in l )      # True

# Indexing a Sequence

x = [10, 20, 30, 40]

print( x[1] )                    # 20

print( x[-1] )                   # 40

print( x[-4: ] )                 # Output is [10, 20, 30, 40]

y = list(range(10))

print(y[-5:])                    # Output is [5,6,7,8,9]

print(y[::2])                    # print every 2nd item

y = [ 1, 2, 3 ]

print(y[0:3])


