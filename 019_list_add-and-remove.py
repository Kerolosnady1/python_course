# Add items to the list:

    # .append()
    # .insert()
    # .extend()


# .append() :
names = ["Kero", "Kerolos", "Yousef", "Mohamed"]

print(names) # ['Kero', 'Kerolos', 'Yousef', 'Mohamed']

print("*" * 30)

names.append("Hassan")

print(names) # ['Kero', 'Kerolos', 'Yousef', 'Mohamed', 'Hassan']

print("*" * 30)

names.append("Tarek")

print(names) # ['Kero', 'Kerolos', 'Yousef', 'Mohamed', 'Hassan', 'Tarek']

print("*" * 30)



# .insert() :

myNumbers = [50, 2, 90, 70, 300]

print(myNumbers) # [50, 2, 90, 70, 300]

print("*" * 30)

myNumbers.insert(1, "Mohamed")

print(myNumbers) # [50, 'Mohamed', 2, 90, 70, 300]

print("*" * 30)


# .extend() :

list_one = ["Kerolos", "Mohamed", "Yousef"]

list_two = [1, 2, 3]

'''list_one.append(list_two)

print(list_one)''' # ['Kerolos', 'Mohamed', 'Yousef', [1, 2, 3]]

list_one.extend(list_two)

print(list_one) # ['Kerolos', 'Mohamed', 'Yousef', 1, 2, 3]


# remove :

    # .remove()
    # .pop()
    # del
    # .clear()

# .remove() :

print("*" * 30)

school_names = ["Mohamed", "Yousef", "Hassan"]

print(school_names) # ['Mohamed', 'Yousef', 'Hassan']

print("*" * 30)

school_names.remove("Mohamed")

print(school_names) # ['Yousef', 'Hassan']


# .pop() :

print("*" * 30)

list_of_numbers = [500, 900, 1001]

print(list_of_numbers) # [500, 900, 1001]

print("*" * 30)

# list_of_numbers.pop(3) # IndexError: pop index out of range

list_of_numbers.pop(1)

print(list_of_numbers) # [500, 1001]


# del :

print("*" * 30)

list_of_names = ["Tarek", "Shenawy", "Araby"]

print(list_of_names) # ['Tarek', 'Shenawy', 'Araby']

print("*" * 30)

del list_of_names[0]

print(list_of_names) # ['Shenawy', 'Araby']


# .clear() :

print("*" * 30)

myNumbersOne = [50, 90, 300, 150, 3.5, 0, True, "Mohamed"]

print(myNumbersOne) # [50, 90, 300, 150, 3.5, 0, True, 'Mohamed']

print("*" * 30)

myNumbersOne.clear()

print(myNumbersOne) # []










































