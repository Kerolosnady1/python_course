# Introduction to sets:
    
    # Syntax of set
    # How to access set
    # How to add items to the set

# set => Unorderd, unchangeable, unindexed.
# var_name = {"apple", 1, False, 5.5}

myset = {"apple", 1, True, 5.5}
print(myset) # {'apple', 1, 5.5}

# True == 1 and 1 == True

print("$" * 50)

myset2 = {"apple", 0, False, 5.5}
print(myset2) # {'apple', 0, 5.5}

# False == 0 and 0 == False

print("$" * 50)

myset3 = {"apple", False, 0, 5.5}
print(myset3) # {'apple', False, 5.5}

print("$" * 50)


# set() => constructor:

myset4 = set(("apple", "banana", "cherry"))
print(myset4) # {'banana', 'cherry', 'apple'}

print("$" * 50)

# How to access items inside the set:

myset5 = {"apple", 1, "banana"}
print("apple" in myset5) # True
print(2 in myset5) # False

print("$" * 50)


# Errors:
'''
myset6 = {'apple', "banana", "cherry"}
myset6[0] = "orange"
print(myset6)
''' # set object doesn't support item assignment

# You can change the set into list, but you cann't also change the value by indexing after the conversion.


# How to add items inside the set:

myset7 = {"apple", "banana", "cherry"}
myset7.add(3)
print(myset7) # {'apple', 3, 'cherry', 'banana'}

print("$" * 50)

# Can you list() to append() or adding items:

myset8 = {1, "apple", 2, "cherry"}

mylist2 = list(myset8)
mylist2.append("banana")
myset8 = set(mylist2)
print(myset8) # {1, 'cherry', 'banana', 2, 'apple'}

print("$" * 50)

# Can also add multiple items:

myset9 = {"apple", "banana", "cherry"}
myset10 = {1 , 2, 3}
myset9.update(myset10)
print(myset9) # {1, 2, 'apple', 'cherry', 3, 'banana'}

print("$" * 50)

# Can add list over set:

myset11 = {"One", "Two", "Three"}
mylist3 = [1, 2, 3, False]

myset11.update(mylist3)

print(myset11) # {1, 2, 'Two', False, 3, 'One', 'Three'}
