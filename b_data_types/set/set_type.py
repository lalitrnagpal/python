s = { 'a', 'c', 'e', 'b', 'd' }
s1 = {'b', 'e', 'd'}
s3 = {'z', 'y', 'x'}

s_copy = s.copy()
print(s_copy)                           # Output {'d', 'a', 'b', 'e', 'c'}

print( s.difference(s1) )               # Output {'a', 'c'}

print( s.intersection(s1) )             # Output {'b', 'e', 'd'}

print( s.isdisjoint(s1) )               # Output False

print( s1.issubset(s) )                 # Output True

print( s1.issubset(s) )                 # Output True

print( s.issuperset(s1) )               # Output True

s.symmetric_difference(s1)              # Output {'a', 'c'}
print( s.symmetric_difference(s1) )

s.union(s1)                                 
print(s)                                # Output {'a', 'c', 'd', 'b', 'e'}

x = 'r'
s.add(x)
print(s)                                # Output {'e', 'c', 'b', 'r', 'd', 'a'}

s.clear()
print(s)                                # Output set()

s = { 'a', 'c', 'e', 'b', 'd' }
s1 = {'b', 'e', 'd'}
s3 = {'z', 'y', 'x'}

x = 'r'
s.discard(x)
print(s)                                # Output {'e', 'c', 'b', 'd', 'a'}

print( s.pop() )                        # Output 'e'

# s.remove(x)                           # KeyError: 'r' - there is no 'r'
s.add(x)
s.remove(x)                             # can remove now
print(s)                                # Output is {'c', 'b', 'd', 'a'}

while s:
   item = s.pop()

print(s)                                # Output set()

