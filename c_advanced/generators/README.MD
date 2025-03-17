# Generators

> When the body of a function contains one or more occurrences of the keyword **yield**, the function is known as a **generator**, or more precisely **a generator function**. 

> When you call a generator, the **function body does not execute**. Instead, the generator function returns a **special iterator object**, known as **a generator object** (sometimes, quite confusingly, also called just “a generator”), **wrapping the function body, its local variables (including parameters), and the current point of execution** (initially, the start of the function).

### Yield Expression

> A bare yield without the expression is also legal, and equivalent to yield None. 

> When yield executes, the function execution is “frozen,” preserving the current point of execution and local variables, and the expression following yield becomes the result of next. 

> When you call next again, execution of the function body resumes where it left off, again up to the next yield. When the function body ends, or executes a return statement, the iterator raises a StopIteration exception to indicate that the iteration is finished. The expression after return, if any, is the argument to the StopIteration exception

> yield is an expression, not a statement. When you call g.send( value ) on a generator object g, the value of yield is value; when you call next(g), the value of yield is None. 

### Building a Iterator

> A generator function is often a handy way to build an iterator

```
for avariable in somegenerator(arguments)
```

> You want a sequence of numbers counting up from 1 to N and then down to 1 again. A generator can help

```
def updown(N):
   for x in range(1, N):
      yield x
   for x in range(N, 0, -1):
      yield x

for i in updown(3):				# Iterator
   print(i) 					# prints: 1 2 3 2 1
```

> Here is a generator that works somewhat like built-in range, but returns an iterator on floating-point values rather than on integers:

```
def frange(start, stop, stride=1.0):
   start = float(start) 			# force all yielded values to be floats
   while start < stop:
      yield start
      start += stride
```

> Generator functions are more flexible than functions that return lists. A generator function may return an unbounded iterator, meaning one that yields an infinite stream of results ( to use only in loops that terminate by other means, e.g., via a conditionally executed break statement ).

> Further, a generator object iterator performs lazy evaluation: the iterator can compute each successive item only when and if needed, “just in time,” while the equivalent function does all computations in advance and may require large amounts of memory to hold the results list. 

> Therefore, if all you need is the ability to iterate on a computed sequence, it is usually best to compute the sequence in a generator object, rather than in a function returning a list. If the caller needs a list of all the items produced by some bounded generator object built by g(arguments), the caller can simply use the following code to explicitly request that Python build a list

```
resulting_list = list( g( arguments ) )
```

### yield from

> To improve execution efficiency and clarity when multiple levels of iteration are yielding values, you can use the form yield from expression, where expression is iterable. This yields the values from expression one at a time into the calling environment, avoiding the need to yield repeatedly

```
def updown(N):
   yield from range( 1, N )
   yield from range( N, 0, -1 )

for i in updown(3):
   print(i)                         # prints: 1 2 3 2 1
```

### Generators as near-coroutines


