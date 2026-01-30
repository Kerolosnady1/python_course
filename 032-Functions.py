# Functions -> DRY (Don't Repeat Yourself)
'''
number1 = 10
number2 = 5

print(number1 * number2) # 50

number1 = 2
number2 = 3

print(number1 * number2) # 6
'''
'''
def multiply(number1, number2): # def -> define / number1 & number2 -> parameters / User defined function (function made by user)
    # print(f"Multiply: {number1 * number2}") # 10 * 5 -> 50
    return number1 * number2 # 10 * 5 -> 50
    print("Hello") # Will not be readed / print() is built-in function


num1, num2 = 10, 5
print(multiply(num1, num2)) # 10 & 5 -> arguments
print(multiply(2, 3)) # 6
# multiply(number2 = 5, number1 = 10)
'''
'''
def add_or_conc(key1, key2):
    return key1 + key2

print(f"Sum: {add_or_conc(5, 2)}") # 7
print(f"Concatenation: {add_or_conc("Hello", " World")}")
'''


# *args and **kwargs
'''
def print_names(*names): # will store the names as a tuple / *names -> packing
    print(f"Type: {type(names)}") # <class 'tuple'>
    print(f"First arg: {names[0]}") # Kerolos
    print(f"Last arg: {names[-1]}") # Ahmed
    print(f"Tuple: {names}") # ('Kerolos', 'Mohamed', 'Ahmed')
    print("Unpacking: ", *names) # Kerolos Mohamed Ahmed
    return


print_names("Kerolos", "Mohamed", "Ahmed")
'''

'''
def sum(a, b, c):
    return a + b + c

numbers = [1, 2, 3]

print(sum(*numbers)) # 6
'''
'''
def name(fname, lname):
    print("Hello,", fname, lname)
    return

person = {"fname" : "Kerolos", "lname": "Nady"}
name(**person)
'''

'''
def myfunc():
    x = 500 # local variable

    def innerfunc():
        print(x)

    innerfunc() # 500

myfunc()
# print(x) will cause an error because it's a local variable not globally used / name 'x' is not defined
'''

x = 500

def myfunc():
    global x
    x = 300
    print(x)

myfunc()

print(x)



























