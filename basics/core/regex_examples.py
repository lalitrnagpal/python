import re

# EXAMPLE 1 - CHECK FOR A VALID PHONE NUMBER

# Using raw string to define a regular expression pattern
def check_valid_date() -> None:
    """Checks for a valid date format """
    pattern = r'\d{3}-\d{3}-\d{4}'

    # Matching the pattern against a string
    text = 'Phone number: 123-456-7890'
    match = re.search( pattern, text )

    if match:
        print('Valid phone number')
    else:
        print('Invalid phone number')

# EXAMPLE - 2 


# EXAMPLE - 3


# EXAMPLE - 4


# Calling all functions

checkValidDate()