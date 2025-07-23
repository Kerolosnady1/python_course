# Introdution, access, and update tuple :

    # Introduction => Syntax:

# Tuple is immutable (unchangable), value inside can be duplicated

names = ("Kerolos", 20, 150.5, True)
print(names) # ('Kerolos', 20, 150.5, True)

print("$" * 50)

print(type(names)) # <class 'tuple'>

print("$" * 50)

school_names = ("'Kerolos', 20, 150.5, True")
print(school_names) # 'Kerolos', 20, 150.5, True

print("$" * 50)

print(type(school_names)) # <class 'str'>

print("$" * 50)

names_two = ("'Kerolos', 20, 150.5, True",)

print(names_two) # ("'Kerolos', 20, 150.5, True",)

print("$" * 50)

print(type(names_two)) # <class 'tuple'>

print("$" * 50)

name_three = (1, 100, 2, 3, 500)

print(name_three) # (1, 100, 2, 3, 500)

print("$" * 50)


# Access The Tuple Items:

names_four = (20, "Kerolos", 5, 9, 7)

print(names_four[1]) # Kerolos

print("$" * 50)

# Slicing :

print(names_four[1:4]) # ('Kerolos', 5, 9)

print("$" * 50)

print(names_four[-1]) # 7

print("$" * 50)


# Updating Items in Tuple:

name_five = ("Kerolos", "Mohamed", "Yousef")

print(name_five) # ('Kerolos', 'Mohamed', 'Yousef')

print("$" * 50)

print(type(name_five)) # <class 'tuple'>

print("$" * 50)

x = list(name_five) # Convert Tuple Into List

print(type(x)) # <class 'list'>

print("$" * 50)

x[1] = "Karim"

print(x) # ['Kerolos', 'Karim', 'Yousef']

print("$" * 50)

name_five = tuple(x)

print(type(name_five)) # <class 'tuple'>

print("$" * 50)

print(name_five) # ('Kerolos', 'Karim', 'Yousef')

print("$" * 50)

'''name_five[1] = "Mohamed"

print(name_five) # 'tuple' object does not support item assignment'''



# .append() :


myFruits = ("Apple", "Banana", "Cherry")

y = list(myFruits) # y = ["Apple", "Banana", "Cherry"]

y.append("Orange")

myFruits = tuple(y)

print(myFruits) # ('Apple', 'Banana', 'Cherry', 'Orange')

print("$" * 50)


# Adding items into tuple:

numbers_one = (1, 2, 3)

z = (4,)

numbers_one += z # numbers_one = numbers_one + z => numbers_one = (1, 2, 3) + (4,)

print(numbers_one) # (1, 2, 3, 4)

print("$" * 50)

print(type(numbers_one))



# .remove() :

print("$" * 50)

names_six = (1,"Kerolos", 2, "Karim")

print(names_six) # (1, 'Kerolos', 2, 'Karim')

print("$" * 50)

e = list(names_six) # Convert names_six from tuple into list and store it in e variable

e.remove("Kerolos")

names_six = tuple(e) # convert e from list into tuple and store it in names_six variable

print(names_six) # (1, 2, 'Karim')



# del

print("$" * 50)

names_seven = ("Mahmoud", 30, "Hany")

print(names_seven) # ('Mahmoud', 30, 'Hany')

del names_seven

# print(names_seven) # Error names_seven is not defined



