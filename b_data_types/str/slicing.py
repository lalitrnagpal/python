# Slicing

mystr = "hello how are you!"

print( mystr[2:5] )             # llo - 2nd to 5th character, index starts at 0

print( mystr[4:] )              # 4th index to the end

print( mystr[:9] )              # 0th index to the 9th index

print( mystr[:-9] )             # leave last 9 characters - same as above basically

print( mystr[1::2] )            # start from 1st index, go to the end, jump by 2

print( mystr[1:9:2] )           # start from 1st index, go to the 9th index, jump by 2