# Exceptions

> The **try** statement is Python’s **core exception handling mechanism**. It’s a compound statement with **three kinds of optional clauses**:

1. It may have **zero or more except clauses**, defining how to handle particular classes of exceptions.

2. If it has except clauses, then it may also have, right afterwards, one **else clause**, executed **only if the try suite raised no exceptions**.

3. Whether or not it has except clauses, it may have **a single finally clause**, **unconditionally executed**, with the behavior covered in **"try/ except/ finally"**.
Python’s syntax **requires the presence of at least one except clause or a finally clause**, both of which might also be present in the same statement; **else is only valid following one or more excepts**.

```
try:
   statement(s)
except [expression [as target]]:
   statement(s)
[else:
   statement(s)]
[finally:
   statement(s)]
```

This form of the try statement has **one or more except clauses**, as well as an **optional else clause** and **an optional finally clause, whose meaning does not depend on whether except and else clauses are present**

The body of each except clause is known as an **exception handler**. 

```
try:
   1/0
   print('not executed')
except ZeroDivisionError:
   print('caught divide-by-0 attempt')
```

**Avoid a “Bare Except” That Doesn’t Re-Raise**

> Exception propagation terminates when it finds a handler whose expression matches the exception object. 

When a try statement is nested (lexically in the source code, or dynamically within function calls) in the try clause of another try statement, a handler established by the inner try is reached first on propagation, so it handles the exception when it matches it. This may not be what you want. 

```
try:
   try:
      1/0
except:
   print('caught an exception')
except ZeroDivisionError:
   print('caught divide-by-0 attempt')
   # prints: caught an exception

```

In this case, it does not matter that the handler established by the clause except ZeroDivisionError: in the outer try clause is more specific than the catch-all except: in the inner try clause. The outer try does not enter into the picture: the exception doesn’t propagate out of the inner try. 

The optional else clause of try/except executes only when the try clause terminates normally. In other words, the else clause does not execute when an exception propagates from the try clause, or when the try clause exits with a break, continue, or return statement. Handlers established by try/except cover only the try clause, not the else clause. The else clause is useful to avoid accidentally handling unexpected exceptions. For example:

```
print(repr(value), 'is ', end=' ')

try:
   value + 0
except TypeError:
   # not a number, maybe a string...?

try:
   value + ''
except TypeError:
   print('neither a number nor a string')
else:
   print('some kind of string')
else:
   print('some kind of number')

try/finally
   Here’s the syntax for the try/finally form of the try statement:
try:
   statement(s)
finally:
   statement(s)
```

> finally clause

The finally clause establishes what is known as a cleanup handler. This code always executes after the try clause terminates in any way. When an exception propagates from the try clause, the try clause terminates, the cleanup handler executes, and the exception keeps propagating. When no exception occurs, the cleanup handler executes anyway, regardless of whether the try clause reaches its end or exits by executing a break, continue, or return statement.

Cleanup handlers established with try/finally offer a robust and explicit way to specify finalization code that must always execute, no matter what, to ensure consistency of program state and/or external entities (e.g., files, databases, network connections). Such assured finalization is nowadays usually best expressed via a context manager used in a with statement (see “The with Statement and Context Managers” on page 201). Here is an example of the try/finally form of the try statement:

```
f = open(some_file, 'w')
try:
   do_something_with_file(f)
finally:
   f.close()

and here is the corresponding, more concise and readable, example of using with for exactly the same purpose:

with open(some_file, 'w') as f:
   do_something_with_file(f)
```

> A try/except/finally statement, such as:

```
try:
   ...   guarded clause...
except ...expression...:
   ...   exception handler code...
finally:
...   cleanup code...
```

is equivalent to the nested statement:

```
try:
   try:
   ...   guarded clause...
   except ...expression...:
   ...   exception handler code...
finally:
   ...   cleanup code...
```

> The raise statement

```
raise [expression [from exception]]
```

Only an exception handler (or a function that a handler calls, directly or indirectly) can use raise without any expression. A plain raise statement re-raises the same exception object that the handler received. The handler terminates, and the exception propagation mechanism keeps going up the call stack, searching for other applicable handlers. Using raise without any expression is useful when a handler discovers that it is unable to handle an exception it receives, or can handle the exception only partially, so the exception should keep propagating to allow handlers up the call stack to perform their own handling and cleanup.

When expression is present, it must be an instance of a class inheriting from the built-in class BaseException, and Python raises that instance. 

Here’s an example of a typical use of the raise statement:

```
def cross_product(seq1, seq2):
   if not seq1 or not seq2:
      raise ValueError('Sequence arguments must be non-empty')
   return [(x1, x2) for x1 in seq1 for x2 in seq2]
```

Some people consider raising a standard exception here to be inappropriate, and would prefer to raise an instance of a custom exception

Once an exception is raised, by Python itself or with an explicit raise statement in your code, it is up to the caller to either handle it (with a suitable try/except statement) or let it propagate further up the call stack. Don’t Use raise for Redundant Error Checks Use the raise statement only to raise additional exceptions for cases that would normally be OK but that your specification defines to be errors. Do not use raise to duplicate the same error checking that Python already (implicitly) does on your behalf.

### The with Statement and Context Managers

The with statement is a compound statement with the following syntax: 

```
with expression [as varname] [, ...]:
   statement(s)
   # 3.10+ multiple context managers for a with statement
   # can be enclosed in parentheses

with (expression [as varname], ...):
   statement(s)
```

The semantics of with are equivalent to:

```
_normal_exit = True
_manager = expression
varname = _manager.__enter__()

try:
   statement(s)
except:
   _normal_exit = False
   if not _manager.__exit_(*sys.exc_info()):
      raise
      # note that exception does not propagate if __exit__ returns
      # a true value
finally:
   if _normal_exit:
      _manager.__exit__(None, None, None)
```

### Exception Propagation

When an exception is raised, the exception propagation mechanism takes control. The normal control flow of the program stops, and Python looks for a suitable exception handler. Python’s try statement establishes exception handlers via its except clauses. The handlers deal with exceptions raised in the body of the try clause, as well as exceptions propagating from functions called by that code, directly or indirectly. If an exception is raised within a try clause that has an applicable except handler, the try clause terminates and the handler executes. When the handler finishes, execution continues with the statement after the try statement 

If the statement raising the exception is not within a try clause that has an applicable handler, the function containing the statement terminates, and the exception propagates “upward” along the stack of function calls to the statement that called the function. If the call to the terminated function is within a try clause that has an applicable handler, that try clause terminates, and the handler executes. Otherwise, the function containing the call terminates, and the propagation process repeats, unwinding the stack of function calls until an applicable handler is found

If Python cannot find any applicable handler, by default the program prints an error message to the standard error stream (sys.stderr). The error message includes a traceback that gives details about functions terminated during propagation. You can change Python’s default error-reporting behavior by setting sys.excepthook.

After error reporting, Python goes back to the interactive session, if any, or terminates if execution was not interactive. When the exception type is SystemExit, termination is silent and ends the interactive session, if any. 

Here are some functions to show exception propagation at work:

```
def f():
   print('in f, before 1/0')
   1/0 # raises a ZeroDivisionError exception
   print('in f, after 1/0')

def g():
   print('in g, before f()')
   f()
   print('in g, after f()')

def h():
   print('in h, before g()')
   try:
      g()
      print('in h, after g()')
   except ZeroDivisionError:
      print('ZD exception caught')
      print('function h ends')

Calling the h function prints the following:

in h, before g()
in g, before f()
in f, before 1/0
ZD exception caught
function h ends

```

That is, none of the “after” print statements execute, since the flow of exception propagation cuts them off.

### Exception Objects

Exceptions are instances of **BaseException** (more specifically, instances of one of its subclasses). 

**cause**

exc.___cause_ Returns the parent exception of an exception raised using raise from. exc. notes

**notes**

3.11+ Returns a list of strs added to the exception using add_note. This attribute only exists if add_note has been called at least once, so the safe way to access this list is with getattr(exc, '__notes___', []).

**add_note**

exc.add_note(note). 3.11+ Appends the str note to the notes on this exception. These notes are shown after the traceback when displaying the exception.

**args**

exc.args - Returns a tuple of the arguments used to construct the exception. This error-specific information is useful for diagnostic or recovery purposes. Some exception classes interpret args and set convenient named attributes on the classes' instances.

**with_traceback**

exc.with_traceback(tb) - Returns a new exception, replacing the original exception's traceback with the new traceback tb, or with no traceback if tb is None. Can be used to trim the original traceback to remove internal library function call frames.

### Hierarchy of standard Exceptions


```
BaseException
    Exception
        AssertionError, AttributeError, BufferError, EOFError, MemoryError, ReferenceError, OsError, StopAsyncIteration, StopIteration, SystemError, TypeError
        ArithmeticError (abstract)
            OverflowError, ZeroDivisionError
        ImportError
            ModuleNotFoundError, ZipImportError
        LookupError (abstract)
            IndexError, КеуЕггог
        NameError
            UnboundLocalError
        OSError
            . . . 
        RuntimeError
            RecursionError
            NotImplementedError
        SyntaxError
            IndentationError
                TabError
        ValueError
            UnsupportedOperation
            UnicodeError
                UnicodeDecodeError, UnicodeEncodeError,
                UnicodeTranslateError
        Warning
            . . .
    GeneratorExit
    KeyboardInterrupt
    SystemExit
```

### Standard Exception Classes

| Exception class | Raised when |
| --------------- | ----------- |
| AssertionError | An assert statement failed. |
| AttributeError | An attribute reference or assignment failed. |
| ImportError | An import or from...import statement (covered in "The import Statement" on page 222) couldn't find the module to import (in this case, what Python raises is actually an instance of ImportError's subclass ModuleNot FoundError), or couldn't find a name to be imported from the module. |
| IndentationError | The parser encountered a syntax error due to incorrect indentation. Subclasses SyntaxError. |
| IndexError | An integer used to index a sequence is out of range (using a noninteger as a sequence index raises TypeError). Subclasses LookupError. |
| KeyboardInterrupt | The user pressed the interrupt key combination (Ctrl-C, Ctrl-Break, Delete, or others, depending on the platform's handling of the keyboard). |
| KeyError | A key used to index a mapping is not in the mapping. Subclasses LookupErгог. | 
| MemoryError | An operation ran out of memory. | 
| NameError | A name was referenced, but it was not bound to any variable in the current scope. | 
| NotImplementedЕггог | Raised by abstract base classes to indicate that a concrete subclass must override a method. |
| OSError | Raised by functions in the module os (covered in "The os Module" on page 343 and "Running Other Programs with the os Module" on page 478) to indicate platform-dependent errors. OSError has many subclasses, covered in the following subsection. |
| RecursionError | Python detected that the recursion depth has been exceeded. Subclasses Runti meError. |
| RuntimeError | Raised for any error or anomaly not otherwise classified. |
| SyntaxError | Python's parser encountered a syntax error. |
| SystemError | Python has detected an error in its own code, or in an extension module. Please report this to the maintainers of your Python version, or of the extension in question, including the error message, the exact Python version (sys.ver sion), and, if possible, your program's source code. |
| ТуреЕггог | An operation or function was applied to an object of an inappropriate type. |
|  UnboundLocalError | A reference was made to a local variable, but no value is currently bound to that local variable. Subclasses Name Error.| 
| UnicodeError | An error occurred while converting Unicode (i.e., a str) to a byte string, or vice versa. Subclasses ValueError. |
| ValueError | An operation or function was applied to an object that has a correct type but an inappropriate value, and nothing more specific (e.g., KeyError) applies. |
| ZeroDivisionError | A divisor (the righthand operand of a /, //, or % operator, or the second argument to the built-in function divmod) is 0. Subclasses ArithmeticErгог. |










