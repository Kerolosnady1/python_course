# Logical Operators:
    
    # not
    # or
    # and

# not :

print(10 == 30) # False

print("*" * 30)

print(not(10 == 30)) # True

print("*" * 30)

number_one = 50
number_two = 100

print(number_one == number_two) # False

print(not(number_one == number_two)) # True

print("*" * 30)

print(number_one < number_two) # True

print(not(number_one < number_two)) # False

print("*" * 30)

txt_one = "Hello"
txt_two = "World"

print(txt_one == txt_two) # False

print(not(txt_one == txt_two)) # True

print("*" * 30)

# or : True => True and False , True and True , False and True

print((10 == 20) or (20 == 20)) # True

print("*" * 30)

print((90 == 90) or (100 == 100)) # True

print("*" * 30)

print((50 == 50) or (10 == 60)) # True

print("*" * 30)

print((10 == 30) or (100 == 200)) # False

print("*" * 30)

print(("Hello" == "World") or (500 == 100) or (10.5 == 10.5)) # True

print("*" * 30)

print(("Hello" == "World") or (500 > 100) or (10.5 < 10.5) or (True != True)) # True

print("*" * 30)

number_three = 600
number_four = 900

print((number_three >= number_four) or (number_three <= number_four)) # True

print("*" * 30)


# and : True => True and True

print((10 == 10) and (100 == 100)) # True

print("*" * 30)

print((10 == 20) and (100 == 100)) # False

print("*" * 30)

print((20 == 30) and (100 == 105)) # False

print("*" * 30)

print((500 == 500) and (500 == 900)) # False

print("*" * 30)

print(("Hello" == "World") and (10.6 >= 10.6) and (True <= True)) # False

print("*" * 30)


# Merge (not, or, and):

print(not(100 == 100) and ((500 > 300) or (True >= True))) # False

print("*" * 30)

print((100 == 100) and ((500 > 300) or (True >= True))) # True



















































