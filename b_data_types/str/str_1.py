s = "Hello There 123"

print( s.capitalize() )	                            # Converts the first character to upper case

print( s.casefold() )	                            # Converts string into lower case

# s = s.center()	                                # Returns a centered string

print( s.count('e') )	                            # Returns the number of times a specified value occurs in a string

print( s.endswith('re')	)                           # Returns true if the string ends with the specified value

print( s.find('llo') )                              # Searches the string for a specified value and returns 
                                                    # the position of where it was found

print ( s.isalnum() )                               # Returns True if all characters in the string are alphanumeric

print( s.isalpha() )                                # Returns True if all characters in the string are in the alphabet

print( s.isascii() )	                            # Returns True if all characters in the string are ascii characters

print( s.isdecimal() )	                            # Returns True if all characters in the string are decimals

print( s.isdigit() )	                            # Returns True if all characters in the string are digits

print( s.isidentifier() )	                        # Returns True if the string is an identifier

print( s.islower() )                                # Returns True if all characters in the string are lower case

print( s.isnumeric() )	                            # Returns True if all characters in the string are numeric

print( s.isspace() )                                # Returns True if all characters in the string are whitespaces

print( s.istitle() )                                # Returns True if the string follows the rules of a title

print( s.isupper() )                                # Returns True if all characters in the string are upper case

# .join()                                           # Converts the elements of an iterable into a string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)                                            # Output is John#Peter#Vicky

# .ljust()                                          # Returns a left justified version of the string

print( s.lower() )                                  # Converts a string into lower case

print( s.lstrip() )                                 # Returns a left trim version of the string

print( s.replace('e', 'i') )                        # Returns a string where a specified value is replaced with a specified value
                                                    # Output is 'Hillo Thiri 123'

print( s.rfind('e') )                               # Searches the string for a specified value and returns the last position of where it was found
                                                    # Output is 10 - the last e in 'Hello There 123'

print( s.rindex('e') )                              # Searches the string for a specified value and returns the last position of where it was found

y = 'Hello'
print(y.rjust(10, '*'))                             # Returns a right justified version of the string. # Output is '*****Hello'

z = "Python is fun, isn't it"                       # .rpartition example
print(z.rpartition('is'))                           # splits at last occurence of 'is'
                                                    # Returns a tuple where the string is parted into three parts

z = 'Python is fun'                                 # Splits the string at the specified separator, and returns a list
print( z.rsplit() )                                 # Output is ['Python', 'is', 'fun'] 

z = 'python    '
print( ':', z.rstrip(), ':' )                       # Returns a right trim version of the string. Output is ': python :'

z = 'Python is fun'                                 # Splits the string at the specified separator, and returns a list
print( z.split() )                                  # Output i ['Python', 'is', 'fun']

z = 'Python \nis \nfun'
print( 'splitlines() ', z.splitlines() )            # Splits the string at line breaks and returns a list

print( s.startswith('a')  )                         #  Returns true if the string starts with the specified value

z = '   python    '
print( z.strip()  )                                 # Returns a trimmed version of the string

z = 'swapcase'                                      # Swaps cases, lower case becomes upper case and vice versa
print( z.swapcase()  )                              # Output would be SWAPCASE

z = 'title'                                         # Converts the first character of each word to upper case
print( z.title() )                                  # Output would be Title

# print( s.translate() )                            # Returns a translated string

z= 'upper'
print( s.upper() )                                  # Converts a string into upper case

s.zfill(30)
print( 'zfill effect ', s, '\'' )                   # Fills the string with a specified number of 0 values at the beginning
