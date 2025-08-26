# Remove and join items in set:

    # Remove:
        
        # .remove()
        # .discard()
        # .pop()

    # Join:
        
        # .union()
        # .intersection()
        # .difference()
        # .symmetric_difference

# Remove:

# .remove() => if not inside the set will raise an error

set1 = {"apple", "banana", "cherry"}
set1.remove("banana")
print(set1) # {'cherry', 'apple'}

print("$" * 50)

'''set2 = {"apple", "banana", "cherry"}
set2.remove("orange")
print(set2)''' # KeyError: orange


# .discard()

set3 = {"apple", "banana", "cherry"}
set3.discard("cherry")
print(set3)

print("$" * 50)

set4 = {"apple", "banana", "cherry"}
set4.discard("orange") # skip this line, because it's not found.
print(set4) # {'apple', 'banana', 'cherry'}

print("$" * 50)

# .clear()

set5 = {"apple", "banana", "cherry"}
set5.clear()
print(set5) # set()

print("$" * 50)


# del

set6 = {"apple", "banana", "cherry"}
del set6
# print(set6) # Error set6 is not defined


# Join:

# .union() => can use with another datatypes like (list, tuple, str, set)
# (|) => | cann't use with set() and another datatype

set7 = {"apple", "banana", "cherry"}
set8 = {1, 2, 3}
list1 = [False]
tuple1 = ("one", "two")

myset = set7.union(set8, list1, tuple1)

print(myset) # {'apple', 1, 2 , False, 'banana', '3', 'two', 'cherry'}

print("$" * 50)
'''
set9 = {"apple", "banana", "cherry"}
set10 = {1, 2, 3}
list2 = [False]
tuple2 = ("one", "two")

myset2 = set9 | set10 | list2 | tuple2

print(myset2) ''' # TypeError: unsupported operand type(s) for |: 'set' and 'list'

set11 = {"apple", "banana", "cherry"}
set12 = {1, 2, 3}

myset3 = set11 | set12

print(myset3) # {'banana', 1, 2, 'cherry', 3, 'apple'}

print("$" * 50)


# .update() => take the original variable and edit the data

set13 = {"a", "b", "c"}
set14 = {1, 2, 3}

set13.update(set14) # like: {"a", "b", "c", 1, 2, 3}

print(set13) # {'a', 2, 'b', 1, 3, 'c'}

print("$" * 50)


# .intersection()

set15 = {1, 3, 5}
set16 = {'a', 'b', 3}

myset4 = set15.intersection(set16)
print(myset4) # {3}

print("$" * 50)


# .intersection_update()

set17 = {1, 3, 5}
set18 = {'a', 'b', 3}

set18.intersection_update(set17)
print(set18) # {3}

print("$" * 50)


# .difference()

set19 = {1, 3, 5}
set20 = {'a', 'b', 3}

myset6 = set19.difference(set20)
print(myset6) # {1, 5}

myset7 = set20.difference(set19)
print(myset7) # {'a', 'b'}

print("$" * 50)


# .difference_update()

set21 = {1 , 2 , 3}
set22 = {"one", "two", 3}

set21.difference_update(set22)
print(set21) # {1, 2}

set22.difference_update(set21)
print(set22) # {'one', 'two'}

print('$' * 50)

# .symmetric_difference()

set23 = {1, 2, 3}
set24 = {1, 'a', 'b'}

myset8 = set23.symmetric_difference(set24)
print(myset8) # {2, 3, 'a', 'b'}

print("$" * 50)

set25 = {1, 2 , 3}
set26 = {1, 'a', 'b'}

set25.symmetric_difference_update(set26)
print(set25) # {2, 'a', 3, 'b}
