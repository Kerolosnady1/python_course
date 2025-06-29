# casting => datatype casting
# int => float
# float => int
# int => str
# float => str

# convert int into float
numberOne = 10
print(numberOne) # 10
print(type(numberOne)) # <class 'int'>
print(float(numberOne)) # 10.0
print(type(float(numberOne))) # <class 'float'>

# convert float into int
numberTwo = 3.9
print(numberTwo) # 3.9
print(type(numberTwo)) # <class 'float'>
print(int(numberTwo)) # 3
print(type(int(numberTwo))) # <class 'int'>

# convert int into str
numberThree = 55
print(numberThree) # 55
print(type(numberThree)) # <class 'int'>
print(str(numberThree)) # 55
print(type(str(numberThree))) # <class 'str'>

print("Hello " + str(numberThree)) # Hello 55
# print("Hello " + numberThree) # typeError

# convert float into str
numberFour = 66.33
print(numberFour) # 66.33
print(type(numberFour)) # <class 'float'>
print(str(numberFour)) # 66.33
print(type(str(numberFour))) # <class 'str'>
