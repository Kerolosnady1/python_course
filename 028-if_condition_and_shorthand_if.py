# If condition, shorthand if, and nested if:


# If condition syntax:
'''
if condition:
    executed statement
'''
if 30 > 100:
    print("30 greater than 100") # will not excuted

if 'kerolos' == 'kerolos':
    print("Yes kerolos is equal kerolos")

print("$" * 50)

if 100 > 200:
    print("No")

elif 100 > 50: # else if
    print("Yes")

print("$" * 50)

if 100 < 200:
    print("Yes")

elif 100 > 200:
    print("No")

print("$" * 50)
'''
if 100 == 200:
print("NO") '''# Error: IndetationError

if 100 == 200:
    print("No")

elif 100 > 200:
    print("No")

else:
    print("No condition excuted")

print("$" * 50)
'''
a = 50
b = "l"

if a > b:
    print("a > b")

elif b > a:
    print("b > a")

else:
    print("a not > b and b not > a")
'''# Error: '>' not support the instance between 'int' and 'str'

x = 10
y = 5.5

if x > y:
    print("x > y") # will be excuted successfully

print("$" * 50)

# shorthand if: => used for readability

if x > y: print("x > y") # will be excuted successfully

print("$" * 50)

# shorthand if, else: => Ternary operator

print("X") if x > y else print("y") # X

print("$" * 50)

print("x") if x < y else print("y") # y

print("$" * 50)


# Nested if condition:

if 10 > 5:
    if 6 > 3:
        if 9 > 1:
            print("All done") # will be excuted

print("$" * 50)

if 10 > 5:
    if 6 > 3:
        if 9 > 10:
            print("All done") # will not be excuted

if 10 > 5:
    if 6 > 3:
        print("Excuted before 9 > 10") # will be excuted
        if 9 > 10:
            print("All done") # will not be excuted

print("$" * 50)

if 10 > 5:
    if 6 > 3:
        if 9 > 10:
            print("All done") # will not be excuted
        print("Excuted before 9 > 10") # will be excuted

print("$" * 50)

if 10 > 5:
    if 6 > 3:
        if 9 > 10:
            print("All done") # will not be excuted
    print("Excuted before 6 > 3") # will be excuted

print("$" * 50)

if 10 > 5:
    print("10 > 5") # will be excuted
    
    if 6 > 3:
        print("6 > 3") # will be excuted
        
        if 9 > 10:
            print("9 > 10") # will not be excuted
        else:
            print("9 not > 10") # will be excuted

    else:
        print("6 not > 3") # will not be excuted

else:
    print("10 not > 5") # will not be excuted

print("$" * 50)

if 10 > 5:
    print("10 > 5") # will be excuted

    if 6 < 3:
        print("6 > 3") # will not be excuted

        if 9 > 10:
            print("9 > 10") # will not be excuted
        else:
            print("9 not > 10") # will not be excuted

    else:
        print("6 not > 3") # will be excuted

else:
    print("10 not > 5") # will not be excuted

print("$" * 50)

# More than one condition per if:

if 10 > 5 and 15 > 2: # True and True => True
    print("Passed")

print("$" * 50)

if 10 < 5 and 15 > 2: # False and True => False
    print("Passed")

else:
    print("Not passed")

print("$" * 50)

if 10 < 5 and 15 < 2: # False and False => False
    print("Passed")

else:
    print("Not passed")

print("$" * 50)

if 10 > 5 or 5 > 10: # True or False => True
    print("Passed")

else:
    print("Not passed")

print("$" * 50)

if 10 > 5 or 12 > 2: # True or True => True
    print("Passed")

else:
    print("Not passed")

print("$" * 50)

if 10 < 5 or 12 < 2: # False or False => False
    print("Passed")

else:
    print("Not passed")

print("$" * 50)

if 10 > 5 and 12 > 2 or 5 < 3: # True and True or False => True , True or False => True
    print("Passed")

else:
    print("Not passed")

