# String Formatter Part 2:

# The Second Case:

# {:s} => string
# {:d} => int => (digit)
# {:f} => float

name = "Kerolos"
language = "Python"
years = 2

print("My name is: {:s}, my language is: {:s}, and my years are: {:d}".format(name,language, years)) # My name is: Kerolos, my language is: Python, and my years are: 2

# {:d} => int => (digit)

myNumber = 10

print("My Number is: {:d}".format(myNumber)) # My Number is: 10

# {:f} => float

print("My Number is: {:f}".format(myNumber)) # My Number is: 10.000000

print("My Number is: {:.3f}".format(myNumber)) # My Number is: 10.000

# Truncate String:

msg = "Hello I love python"

print("This is long Message: {:s}".format(msg)) # This is long Message: Hello I love python

print("This is a Short Message: {:.5s}".format(msg)) # This is a Short Message: Hello


# Number Format:

number = 500000

print("My number is: {:d}".format(number)) # My number is: 500000

print("My number is: {:_d}".format(number)) # My number is: 500_000

print("My number is: {:,d}".format(number)) # My number is: 500,000

numOne = 50000
numTwo = 300000
numThree = 10

print("One: {:,d} , Two: {:,d} , and Three: {:,d}".format(numOne,numTwo,numThree))
'''One: 50,000 , Two: 300,000 , and Three: 10'''


one = 10
two = 99
three = 2.5

print("One: {1:d} , Two: {2:.2f} , Three: {0:d}".format(one,two,three))
'''One: 99 , Two: 2.50 , Three: 10'''


print("One: {} , Two: {} , Three: {}".format(one,two,three))
'''One: 10 , Two: 99 , Three: 2.5'''

print("One: {2} , Two: {0} , Three: {1}".format(one,two,three))
'''One: 2.5 , Two: 10 , Three: 99'''
