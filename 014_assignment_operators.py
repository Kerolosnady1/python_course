# Assignment Operators:

    # =
    # +=
    # -=
    # *=
    # /=
    # **=
    # /=
    # %=
    # //=

# = :

number = 10 # Assign the value (10) into the variable name (number)


# += :

numberOne = 10
numberOne += 20 # numberOne = numberOne + 20 => numberOne = 10 + 20 = 30
print(numberOne) # 30

print("=" * 30)

# -= :

numberTwo = 0
numberTwo -= 3 # numberTwo = numberTwo - 3 => 0 - 3 = -3
print(numberTwo) # -3

x = 15
y = 3

print("=" * 30)

x -= y # x = x - y => x = 15 - 3 = 12
print(x) # 12

print("=" * 30)

# *= :

numberThree = 5
numberThree *= 20 # numberThree = numberThree * 20 => numberThree = 5 * 20 = 100
print(numberThree) # 100

'''numberFour *= 6 # numberFour = numberFour * 6
print(numberFour) # nameError : name 'numberFour' is not defined'''

print("=" * 30)


# /= :

numberFive = 10
numberFive /= 5 # numberFive = numberFive / 5 => numberFive = 10 / 5

typecasting = int(numberFive) # Convert (numberFive) from <class 'float'> into <class 'int'>

print(numberFive) # 2.0

print(type(numberFive)) # <class 'float'>

print("=" * 30)

print(typecasting) # 2
print(type(typecasting)) # <class 'int'>

print("=" * 30)

# **= :

numberSix = 5
numberSix **= 2 # numberSix = numberSix ** 2 => numberSix = 5 ** 2 => 5 * 5 = 25
print(numberSix) # 25

print("=" * 30)

# %= :

numberSeven = 6
numberSeven %= 2 # numberSeven = numberSeven % 2 => numberSeven = 6 % 2 = 0 => 6 / 2 = 3, remainder = 0
print(numberSeven) # 0

print("=" * 30)

# //= :

numberEight = 6
numberEight //= 3.5 # numberEight = numberEight // 3.5 => numberEight = 6 // 3.5 = 1 => 6 / 3.5 = 1.6667
print(numberEight) # 1.0

print("=" * 30)

numberNine = 6
floorDivision = 3.5
print(numberNine / floorDivision) # 6 / 3.5 = 1.7

print(numberNine // floorDivision) # 6 // 3.5 = 1.0

print(int(numberNine / floorDivision)) # 6 / 3.5 = 1

print(int(float(numberNine / floorDivision))) # 6 / 3.5 = 1

print("=" * 30)

# How the floor division (//) works:

numberTen = 6
floorD = 3.5

fDivision = numberTen / floorD # 6 / 3.5 = 1.7
print(int(fDivision)) # 1 => convert (1.7) into (1)

convert = int(fDivision) # Convert (1.7) into (1) and save it into (convert) variable
print(float(convert)) # 1.0
