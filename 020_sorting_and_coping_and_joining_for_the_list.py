# Sorting, Coping, and Joining:

    # .sort()
    # .sort(reverse = True)
    # .copy()
    # list()
    # list_one + list_two + ...

# .sort() : => ascending order => 1,..,100 or a,...,z or A,...,Z

list1 = ["a", "b", "d", "c", "z", "p"]

print(list1) # ['a', 'b', 'd', 'c', 'z', 'p']

print("$" * 50)

list1.sort()

print(list1) # ['a', 'b', 'c', 'd', 'p', 'z']

print("$" * 50)

list2 = ["Kerolos", "Ahmed", "Mohmaed", "Yousef", "Zien"]

print(list2) # ['Kerolos', 'Ahmed', 'Mohamed', 'Yousef', 'Zien']

print("$" * 50)

list2.sort()

print(list2) # ['Ahmed', 'Kerolos', 'Mohamed', 'Yousef', 'Zien']

print("$" * 50)

list3 = ["Mohamed", "Ahmed", "kerolos", "yousef", "Zein"]

print(list3) # ['Mohamed', 'Ahmed', 'kerolos', 'yousef', 'Zien']

print("$" * 50)

list3.sort() # sort case insensetive

print(list3) # ['Ahmed', 'Mohamed', 'Zien', 'kerolos', 'yousef']

print("$" * 50)

list4 = [1 , 2, 1.5, 6, 3, 80]

print(list4) # [1, 2, 1.5, 6, 3, 80]

print("$" * 50)

list4.sort()

print(list4) # [1, 1.5, 2, 3, 6, 80]

print("$" * 50)

list5 = ["a", 1, "b", 2, "C", 3, "D", 4, "e", 5]

print(list5) # [a', 1, 'b', 2, 'C', 3, 'D', 4, 'e', 5]

print("$" * 50)

# list5.sort() # TypeError: '<' not supported between instances of 'int' and 'str'


# .sort(reverse = True) : descending order => 100,...,1 or z,...,a or Z,...,A

list6 = [1, 200, 3, 500, 8.3, 19]

print(list6) # [1, 200, 3, 500, 8.3, 19]

print("$" * 50)

list6.sort(reverse = True) # [1, 3, 8.3, 19, 200, 500] => [500, 200, 19, 8.3, 3, 1]

print(list6) # [500, 200, 19, 8.3, 3, 1]

print("$" * 50)

list7 = ["a", "b", "A", "Z", "z", "c", "B"]

print(list7) # ["a", "b", "A", "Z", "z", "c", "B"]

print("$" * 50)

list7.sort(reverse = True) # case insensetive

print(list7) # ['A', 'B', 'Z', 'a', 'b', 'c', 'z'] => ['z', 'c', 'b', 'a', 'Z', 'B', ''A]


# .copy() : => take a copy from the original to prevent damage the original

print("$" * 50)

list8 = ['a', 'b', 'c']

print(list8) # ['a', 'b', 'c']

print("$" * 50)

list9 = []

print(list9) # []

list9 = list8.copy()

list9.append("d")

list9.append("e")

print("$" * 50)

print(list8) # ['a', 'b', 'c']

print("$" * 50)

print(list9) # ['a', 'b', 'c', 'd', 'e']

# Memory => list8 (['a', 'b', 'c'])

# Memory => list9 = list8 => list9 = address(list8) + value inside the list8

# When you change the value of list9 then the list8 will change ether

# Whle you use .copy() method you will copy the value of list8 not the address of list8


# list() : => convert (str, tuple, set, ...)

print("$" * 50)

name = "Kerolos" # K e r o l o s => sequence of characters

print(name) # Kerolos

print("$" * 50)

# list(name) # logical Error => Kerolos

print(list(name)) # convert from str into list # ['K', 'e', 'r', 'o', 'l', 'o', 's']


# join :

print("$" * 50)

list12 = ['a', 'b', 'c']

list13 = [1, 2, 3]

list14 = list12 + list13 # Join

print(list14) # ['a', 'b', 'c', 1, 2, 3]

print("$" * 50)

list15 = list13 + list12

print(list15) # [1, 2, 3, 'a', 'b', 'c']

print("$" * 50)

list16 = [1, 2, 3]

list17 = ['a', 'b', 'c']

list18 = [5.5, 3.2, 8.1]

list19 = list16 + list18 + list17

print(list19) # [1, 2, 3, 5.5, 3.2, 8.1, 'a', 'b', 'c']




