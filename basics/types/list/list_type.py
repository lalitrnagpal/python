from collections import deque

# List

## a list is a built-in dynamic sized array
## We can store all types of items (including another list) in a list
## A list may contain mixed type of items, this is possible because a list mainly 
## stores references at contiguous locations and actual items maybe stored at different locations.

## List can contain duplicate items.
## List in Python are Mutable. Hence, we can modify, replace or delete the items.
## List are ordered. It maintain the order of elements based on how they are added.
## Accessing items in List can be done directly using their position (index), starting from 0.

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
morefruits = ['pineapple', 'chickoo']

# append() - Adds an element at the end of the list
fruits.append('grape')

print(fruits)   # Output ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape']

# clear() and copy() - Removes all the elements from the list. copy() - Returns a copy of the list

copy_of_fruits = fruits.copy()
copy_of_fruits.clear()

print('copy_of_fruits: ', copy_of_fruits)           
# Output - copy_of_fruits:  []

print('fruits: ', fruits)                           
# Output - ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape', 'pineapple', 'chickoo']

# count() - Returns the number of elements with the specified value

fruits.count('apple')                               # Output is 2
fruits.count('tangerine')                           # Output is 0

# extend() - Add the elements of a list (or any iterable), to the end of the current list

fruits.extend( morefruits )
print(fruits)

# index() - Returns the index of the first element with the specified value

fruits.index('banana')     # Output is 3

fruits.index('banana', 4)  # Find next banana starting at position 4. Output is 6

# insert() - Adds an element at the specified position
fruits.insert(4, 'papaya')
print('after adding papaya: ', fruits)
# Output is after adding papaya:  
# ['orange', 'apple', 'pear', 'banana', 'papaya', 'kiwi', 'apple', 'banana', 'grape', 'pineapple', 'chickoo']

# pop() - Removes the element at the specified position

fruits.pop()            # Output 'pear'

# remove() - Removes the first item with the specified value

fruits.remove('kiwi')
print('After removing kiwi', fruits )

# reverse() - Reverses the order of the list

fruits.reverse()
print( fruits )     
# Output - ['pineapple', 'grape', 'banana', 'apple', 'banana', 'pear', 'apple', 'orange']

# sort() - Sorts the list

fruits.sort()
print( fruits )
# Output - ['apple', 'apple', 'banana', 'banana', 'grape', 'orange', 'pear', 'pineapple']

### Using **Lists as Stacks**

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print( stack )
# Output is [3, 4, 5, 6, 7]

print( stack.pop() )
# Output is 7

print( stack )
# Output is [3, 4, 5, 6]

print( stack.pop() )
# Output is 6

print( stack.pop() )
# Output is 5

print( stack )
# Output is [3, 4]

### Using **Lists as Queues**

# from collections import deque - specified at the top

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")           # Terry arrives

queue.append("Graham")          # Graham arrives

print( queue.popleft() )                 # The first to arrive now leaves
# Output is 'Eric'

print( queue.popleft() )                 # The second to arrive now leaves
# Output is 'John'

print( queue )                           # Remaining queue in order of arrival
# Output is deque(['Michael', 'Terry', 'Graham'])



