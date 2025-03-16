list from range 0 to 10

list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_)

# Simple Examples

filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums(): ", filter_nums("Geeks101"))
# Output: filter_nums(): Geeks

do_exclaim = lambda s: s + '!'
print("do_exclaim(): ", do_exclaim("I am tired"))
# Output: do_exclaim(): I am tired!

# Accepts n as a string and then iterates on all numbers in it and sums them
find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum(): ", find_sum(101))
# Output: find_sum(): 2

# lambda function

lambda_list = list( map( lambda x: x * 2, list_) )

# Map basically iterates every element in the list_ and returns the lambda function result

print(lambda_list)

# list comprehension

list_comp = [x * 2 for x in list_]
print(list_comp)

# Output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]







