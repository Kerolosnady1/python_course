# int => integer
# float => floating point number
# complex => complex number (Number and Letter)

# int
numberOne = 10
print(type(numberOne)) # <class'int'>

numberTwo = -10
print(type(numberTwo)) # <class 'int'>

numberThree = 123456789101112
print(type(numberThree)) # <class 'int'>

numberFour = -123456789101112
print(type(numberFour)) # <class 'int'>

# float
floatOne = 3.5
print(type(floatOne)) # <class 'float'>

floatTwo = -6.2
print(type(floatTwo)) # <class 'float'>

floatThree = 123456.7891011
print(type(floatThree)) # <class 'float'>

floatFour = -123456.7891011
print(type(floatFour)) # <class 'float'>

# complex
complexOne = 1j
print(type(complexOne)) # <class 'complex'>

complexTwo = 1+5j
print(complexTwo) # (1+5j)
print(type(complexTwo)) # <class 'complex'>

'''complexThree = 5p
print(complexThree) # syntaxError'''

complexFour = 6/3j
print(complexFour) # -2j
print(type(complexFour)) # <class 'complex'>

complexFive = 2*2j
print(complexFive) # 4j
print(type(complexFive)) # <class 'complex'>

complexSix = -3j
print(complexSix) # (-0-3j)
print(type(complexSix)) # <class 'complex'>
