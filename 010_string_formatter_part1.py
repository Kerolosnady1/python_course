# String Formatter Before Version 3.6

# First Case of string formatter:

# Place Holders:
# %s => string
# %d => int => (digit)
# %f => float

name = "Kerolos"
language = "C++"
year = "1"

print("My name is: %s, my language is: %s, and my year is: %s" % (name, language, year))
'''My name is: Kerolos, my language is: C++, and my year is: 1'''

# %d => int

myNumber = 10

print("My Number is: %d" % myNumber) # My Number is: 10

# %f => float

print("My Number is: %f" % myNumber) # My Number is: 10.000000

print("My Number is: %.2f" % myNumber) # My Number is: 10.00


# Truncate String

msg = "Hello my name is Kerolos"

print("This is a Message: %s" % msg) # This is a Message: Hello my name is Kerolos

print("This is a Short Message: %.5s" % msg) # This is a Short Message: Hello














