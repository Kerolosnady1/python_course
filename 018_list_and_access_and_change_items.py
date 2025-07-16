# Intro To List and How to access or change items inside:

    # List
    # Access Items Inside The List
    # Change The Items Inside The List

# List : mutable(Changable) data type , can has multiple data types inside(boolean, string, float, etc...)

'''
myName = "Kerolos"
myAge = 20
myAddress = "6 October"

'''

myInfo = ["Kerolos", 20, "6 October", 200.5, True] # String & Integer & Float & Boolean
print(myInfo) # ['Kerolos', 20, '6 October', 200.5, True]

print("*" * 60)

mylistOne = [10,20,30,40,50] # Integers
print(mylistOne) # [10, 20, 30, 40, 50]

print("*" * 60)

mylistTwo = ["Hi", "Hello", "Welcome"] # Strings
print(mylistTwo) # ['Hi', 'Hello', 'Welcome']

print("*" * 60)

mylistThree = [10.5 , 30.6, 90.9, 5.1] # Floats
print(mylistThree) # [10.5, 30.6, 90.9, 5.1]

print("*" * 60)

mylistFour = [True, False, True , True, False] # Booleans
print(mylistFour) # [True, False, True, True, False]

print("*" * 60)

mylistFive = ['Kerolos', 'Nady', 'Gerges']
print(mylistFive) # ['Kerolos', 'Nady', 'Gerges']

print("*" * 60)


# Access List Items :

myData = ["Kerolos", 20, "6 October", 200.5, True]
print(type(myData)) # <class 'list'>
print(myData[0]) # Kerolos

print("*" * 60)

print(myData[-1]) # True

print("*" * 60)

print(myData[-2]) # 200.5

print("*" * 60)

print(myData[1]) # 20

print("*" * 60)

print(myData[1:]) # [20, '6 October', 200.5, True]

print("*" * 60)

print(myData[2:4]) # ['6 October', 200.5]

print("*" * 60)

print(myData[:3]) # ['Kerolos', 20, '6 October']


print("*" * 60)


# Change List Items :

myFruit = ["Apple", "Banana", "Water Melon"]

print(myFruit) # ['Apple', 'Banana', 'Water Melon']

print("*" * 60)

myFruit[0] = "IPhone" # Updated Value 'Apple' With 'IPhone'

print(myFruit) # ['IPhone', 'Banana', 'Water Melon']

print("*" * 60)

myNumbers = [10, 20, 30, 5, 100]

print(myNumbers) # [10, 20, 30, 5, 100]

print("*" * 60)

myNumbers[2] = 90 # Updated Value 30 With 90

print(myNumbers)

print("*" * 60)

# myNumbers[1:4] = 50 # Error

myNumbersOne = [50]

myNumbers[1:4] = myNumbersOne

print(myNumbers) # [10, 50, 100]

print("*" * 60)

myNumbers[1] = [20, 30, 40]

print(myNumbers) # [10, [20, 30, 40], 100]

print("*" * 60)

myNumbersTwo = [20, 30, 40]

myNumbers[1] = myNumbersTwo

print(myNumbers) # [10, [20, 30, 40], 100]

print("*" * 60)

print(myNumbers[1][0]) # 20 => Multy Dimensional List






















