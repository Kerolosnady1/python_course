# Comparison Operators
    
    # == (Equal)
    # > (Greater Than)
    # < (Smaller Than)
    # != (Not Equal)
    # <= (Smaller Than OR Equal)
    # >= (Greater Than OR Equal)

# == : => equal

print(10 == 10) # True

print("#" * 30)

print(10 == 9) # False

print("#" * 30)

print("Kero" == "Kero") # True

print("#" * 30)

print('Kero' == "Kero") # True

print("#" * 30)

print("l" == "l") # True

print("#" * 30)

print("L" == "l") # False

print("#" * 30)

print(True == True) # True

print("#" * 30)

print(False == True) # False

print("#" * 30)

print(True == False) # False

print("#" * 30)

nameOne, nameTwo = "Kero", "Ahmed"

print(nameOne == nameTwo) # False

print("#" * 30)

result = nameOne == nameTwo

print(result) # False

print(int(result)) # 0 => convert the boolean value into integer value

print("#" * 30)

nameThree, nameFour = "Kero", "Kero"

print(nameThree == nameFour) # True

rs = nameThree == nameFour

print(rs) # True

print(int(rs)) # 1

print("#" * 30)


# > : => greater than

print(50 > 100) # False

print("#" * 30)

print(100 > 3) # True

print("#" * 30)

print("Kero" > "Ahmed") # True

print("#" * 30)

print("Ahmed" > "Kero") # False

print("#" * 30)

print("Ahmed" > "kero") # False

print("#" * 30)

print("k" > "a") # True

print("#" * 30)

numberOne, numberTwo = 10.5, 10.5

print(numberOne > numberTwo) # False

print("#" * 30)

numberThree, numberFour = 60, 100

print(numberThree > numberFour) # False

print("#" * 30)

print(numberFour > numberThree) # True

print("#" * 30)


# < : => smaller than

print(100 < 200) # True

print("#" * 30)

print(500 < 200) # False

print("#" * 30)

print(30 < 30) # False

print("#" * 30)

print('a' < "k") # True

print("#" * 30)

print('A' < 'k') # True

print("#" * 30)

print("Kero" < "Mohamed") # True

print("#" * 30)


# != : => not equal

print(50 != 50) # False

print("#" * 30)

print(10 != 5) # True

print("#" * 30)

print("Kero" != "Mohamed") # True

print("#" * 30)


# <= : => smaller than or equal

print(50 <= 50) # True

print("#" * 30)

print(50 <= 30) # False

print("#" * 30)

print("Kero" <= "Kero") # True

print("#" * 30)


# >= : => greater than or equal

print(900 >= 500) # True

print("#" * 30)

print("Kero" >= "Mohamed") # False

print("#" * 30)

print("Mohamed" >= "Kero") # True

print("#" * 30)

# For Knowledge :

# print(50 !< 30) # Error

# print(!(50 < 30)) # Error

print(not(50 < 30)) # True

print("#" * 30)

print(not(50 > 30)) # False

# print(50 !> 30) # Error

# print(!(50 > 30)) # Error


























