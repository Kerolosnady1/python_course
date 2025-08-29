# Introduction to dictionaries, syntax, length and how to use dict() constructor

    # syntax
    # access items
    # change items

# syntax, length, and dict() constructor:

# ordered, changeable, accessable, and don't allow duplicate

mydict = {"name":"Kerolos", "age":20, "mood":"Happy"}
print(mydict) # {'name':'Kerolos', 'age':20, 'mood':'Happy'}
print(len(mydict)) # 3

print("$" * 50)

mydict1 = {"name":"Kerolos", "age":20, "mood":"Happy", "age":21}
print(mydict1) # {'name':'Kerolos', 'age':21, 'mood':'Happy'}

print("$" * 50)

print(type(mydict1)) # <class 'dict'>

print("$" * 50)

mydict2 = {
        "brand":"Ford",
        "model":"Mustang",
        "year":1964,
        "list":['red', 'blue']
        }
print(mydict2) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'list': ['red', 'blue']}

print("$" * 50)

mydict3 = dict(name = "Kerolos", age = 21)
print(mydict3) # {'name':'Kerolos', 'age':21}

print("$" * 50)

# Access items:

mydict4 = {'name':'Kerolos', 'age':21}
print(mydict4['age']) # 21

print("$" * 50)
'''
mydict5 = {'name':'Kerolos', 'age':21}
print(mydict5[21])''' # KeyError: 21

print("$" * 50)

mydict6 = {'name':'Mohamed', 'age':20}
print(mydict6['name']) # Mohamed

print("$" * 50)

mydict7 =  {'name':'Mohamed', 'age':20}
x = mydict7.get('age') # mydict7['age']
print(x) # 20

print("$" * 50)

mydict8 = {'name':'Mohamed', 'age':20}
print(mydict8.get('age')) # 20

print("$" * 50)

mydict9 = {

        "brand":"Ford",
        "model":"Mustang",
        "year":1964
        }

print(mydict9.keys()) # dict_keys(['brand', 'model', 'year'])

print("$" * 50)

mydict10 = {

        "brand":"Ford",
        "model":"Mustang",
        "year":1964
        }

print(mydict10.values()) # dict_values(['Ford', 'Mustang', 1964])

print("$" * 50)

mydict11 = {

        "brand":"Ford",
        "model":"Mustang",
        "year":1964
        }
print(mydict11.items()) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

print("$" * 50)

mydict12 = {
        "brand":"Ford",
        "model":"Mustang",
        "year":1964
        }
print('model' in mydict12) # True
print('Ford' in mydict12) # False

print("$" * 50)


# Change value:

mydict13 = {"name":"Kerolos", 'age':20}
mydict13['age'] = 21
print(mydict13) # {'name':'Kerolos', 'age':21}

print("$" * 50)

mydict14 = {"name":"Kerolos", 'age':20}
mydict14.update(['age':21])
print(mydict14) # {'name':'Kerolos', 'age':21}
