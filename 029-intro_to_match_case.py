# Introduction to match case syntax, and how to use it

# Syntax:

match 3:

    case 1:
        print("Sunday")

    case 2:
        print("Monday")

    case 3:
        print("Tuesday") # this case will be excuted

    case 4:
        print("Wednesday")


print("$" * 50)

number = 1

match number:

    case 1:
        print("case 1") # will be excuted

    case 2:
        print("case 2")

    case 3:
        print("case 3")

print("$" * 50)

match 5:

    case 1:
        print("case 1")

    case 2:
        print("case 2")

    case _:
        print("No cases found!")

print("$" * 50)


# combine values:

match 4:

    case 1 | 2 | 3 | 4 | 5:
        print("Hello")

    case 6 | 7:
        print("Not hello.")

    case _:
        print("Not found")

print("$" * 50)

month = 5

day = 4

match day:

    case 1 | 2 | 3 | 4 | 5 if month == 4: # True and False = False
        print("Weekend") # Will not excute

    case 1| 2 | 3 | 4 | 5 | 6 | 7 if month == 5: # True and True = True
        print("Work day") # Will be excuted

    case _:
        print("Not found")
