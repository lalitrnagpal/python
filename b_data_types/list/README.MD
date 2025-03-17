# List

> A list is a **built-in dynamic sized array**. <br>
We **can store all types of items** (**including another list**) in a list <br>
A list may contain **mixed type of items**, this is possible because a list mainly <br>
**stores references at contiguous locations** and **actual items maybe stored at different locations**.<br>
<br>
List can contain **duplicate items**.<br>
List in Python are **Mutable**. Hence, we can modify, replace or delete the items.<br>
List are **ordered**. It maintain the order of elements **based on how they are added**.<br>
**Accessing items** in List can be done directly **using their position (index)**, starting from 0.<br>

> **Creating a List**

```
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
morefruits = ['pineapple', 'chickoo']
```

> **append()** - Adds an element at the end of the list

```
fruits.append('grape')

print(fruits)   # Output ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape']
```

> **clear() and copy()** - Removes all the elements from the list. copy() - Returns a copy of the list

```
copy_of_fruits = fruits.copy()
copy_of_fruits.clear()

print('copy_of_fruits: ', copy_of_fruits)           
# Output - copy_of_fruits:  []

print('fruits: ', fruits)                           
# Output - ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape', 'pineapple', 'chickoo']
```

> **count()** - Returns the number of elements with the specified value

```
fruits.count('apple')                               # Output is 2
fruits.count('tangerine')                           # Output is 0
```

> **extend()** - Add the elements of a list (or any iterable), to the end of the current list

```
fruits.extend( morefruits )
print(fruits)
```

> **index()** - Returns the index of the first element with the specified value

```
fruits.index('banana')     # Output is 3

fruits.index('banana', 4)  # Find next banana starting at position 4. Output is 6
```

> **insert()** - Adds an element at the specified position

```
fruits.insert(4, 'papaya')
print('after adding papaya: ', fruits)
# Output is after adding papaya:  
# ['orange', 'apple', 'pear', 'banana', 'papaya', 'kiwi', 'apple', 'banana', 'grape', 'pineapple', 'chickoo']
```

> **pop()** - Removes the element at the specified position

```
fruits.pop()            # Output 'pear'
```

> **remove()** - Removes the first item with the specified value

```
fruits.remove('kiwi')
print('After removing kiwi', fruits )
```

> **reverse()** - Reverses the order of the list

```
fruits.reverse()
print( fruits )

# Output - ['pineapple', 'grape', 'banana', 'apple', 'banana', 'pear', 'apple', 'orange']
```

> **sort()** - Sorts the list

```
fruits.sort()
print( fruits )
# Output - ['apple', 'apple', 'banana', 'banana', 'grape', 'orange', 'pear', 'pineapple']
```

> Using **Lists as Stacks**

```
stack = [3, 4, 5]
stack.append(6)
stack.append(7)

stack
[3, 4, 5, 6, 7]
```

```
stack.pop()
7

stack
[3, 4, 5, 6]
```

```
stack.pop()
6
```

```
stack.pop()
5
```

```
stack
[3, 4]
```

> Using **Lists as Queues**

```
from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")           # Terry arrives

queue.append("Graham")          # Graham arrives

queue.popleft()                 # The first to arrive now leaves
'Eric'

queue.popleft()                 # The second to arrive now leaves
'John'

queue                           # Remaining queue in order of arrival

deque(['Michael', 'Terry', 'Graham'])
```

> **Convert a nested list into a flat list**

```
# Original list
lis = [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]

# iterate through the sublist using List comprehension
flatList = [element for innerList in lis for element in innerList]

# printing original list
print('List', lis)
# Output: # List [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]

# printing flat list
print('Flat List', flatList)
# Output: # Flat List [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
```




