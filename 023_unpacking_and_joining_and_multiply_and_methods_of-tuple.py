# Unpacking, Unpacking Using Asterisk (*), Joining, Multply, and Methods About Tuples:

    # Unpacking
    # Unpacking using asterisk
    # Joining Two or more tuples
    # Two Methods


# Unpacking:

fruits = ("Apple", "Banana", "Cherry")
(green, yellow, red) = fruits

print(green) # Apple
print(yellow) # Banana
print(red) # Cherry

print("$" * 50)

'''names = ("Kerolos", "Mohamed", "Yousef")
names = kero, mo, joe

print(kero)
print(mo)
print(joe)''' # Error


school_names = ("Kerolos", "Mohamed", "Yousef")

name1, name2, name3 = school_names

print(name1) # Kerolos
print(name2) # Mohamed
print(name3) # Yousef

print("$" * 50)


# Unpacking Using Asterisk (*):

univ_names = ("Kerolos", "Mohamed", "Yousef", "Karim", "Tarek")

name4, *name5, name6 = univ_names # name5 converted from tuple into list to let the data be changable

print(name4) # Kerolos
print(name5) # ['Mohamed', 'Yousef', 'Karim']
name5 = tuple(name5) # new version of converting
# x = tuple(name5) # old version of converting
print(name5) # ('Mohamed', 'Yousef', 'Karim')
print(name6) # Tarek

print("$" * 50)


# Joining:

alpha = ("a", "b", 'c')
numeric = (1, 2, 3)

total_tuple = alpha + numeric

print(total_tuple) # ('a', 'b', 'c', 1, 2, 3)

print("$" * 50)

alpha2 = ('a', 'b', 'c')
numeric2 = (1, 2, 3)

total_tuple2 = numeric2 + alpha2

print(total_tuple2) # (1, 2, 3, 'a', 'b', 'c')

print("$" * 50)


# Muliply Tuples:

number_one = (1, 5, 9, 13)
store_number_one = number_one * 3

print(store_number_one) # (1, 5, 9, 13, 1, 5, 9, 13, 1, 5, 9, 13)

print("$" * 50)


# Methods:
    # .count()
    # .index()

# .count()

fruits_one = ("Apple", "Banana", "Banana", "One", "Two", 1)

print(fruits_one.count("Banana")) # 2

print(fruits_one.count(1)) # 1

print(fruits_one.count("One")) # 1


print("$" * 50)


# .index()


numbers_two = (1, 1, 3, 1, 5, 5, 6, 1)

print(numbers_two.index(1)) # 0

print(numbers_two.index(3)) # 2

print(numbers_two.index(5)) # 4
