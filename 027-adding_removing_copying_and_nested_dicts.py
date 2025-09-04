# How to add, remove, copy, and work with nested loop

    # Add:
        
        # index[name] = 'value'
        # .update()

    # Remove:
        
        # .pop()
        # .popitem()
        # del
        # .clear()

    # Copy:
        
        # .copy()

    # Nested dicts:

# Add:


thisdict = {
        'brand':'Ford',
        'model':'Mustang',
        'year':1964
        }

thisdict['color'] = 'blue'
print(thisdict) # {'brand':'Ford', 'model':'Mustang', 'year':1964, 'color':'blue'}

print("".center(50, "$"))

thisdict.update({'speed':280})
print(thisdict) # {'brand':'Ford', 'model':'Mustang', 'year':1964, 'color':'blue', 'speed':280}

print("".center(50, "$"))


# Remove:

thisdict2 = {
        'brand':'Ford',
        'model':'Mustang',
        'year':1964,
        'color':'blue'
        }

thisdict2.pop('model')
print(thisdict2) # {'brand':'Ford', 'year':1964, 'color':'blue'}

print("$" * 50)

thisdict2.popitem()
print(thisdict2) # {'brand':'Ford', 'year':1964}

print("$" * 50)

thisdict3 = {
        'brand':'Ford',
        'model':'Mustang',
        'year':1964,
        'color':'blue'
        }
thisdict3.popitem()
print(thisdict3)

print("$" * 50)

thisdict3.clear()
print(thisdict3) # {}

print("$" * 50)

thisdict4 = {
        'brand':'Ford',
        'model':'Mustang',
        'year':1964,
        'color':'blue'
        }
del thisdict4 # => can also use del to delete one item like: del thisdict4['model']

# print(thisdict4) # Will print an Error: name 'thisdict4' is not defined

# Copying:

# mydict = thisdict4 # will cause an error

thisdict5 = {
        'brand':'Ford',
        'model':'Mustang',
        'year':1964,
        'color':'blue'
        }

mydict = thisdict5.copy()
mydict.pop('model')
print(mydict) # {'brand':'Ford', 'year':1964, 'color':'blue'}

print("$" * 50)

print(thisdict5) # {'brand':'Ford', 'model':'Mustang', 'year':1964, 'color':'blue'}

print("$" * 50)

mydict2 = dict(thisdict5)
print(mydict2) # {'brand':'Ford', 'model':'Mustang', 'year':1964, 'color':'blue'}

print("$" * 50)


# Nested dict:

myfamily = {
        'child1' : {'name':'Kero', 'year':21},
        'child2' : {'name': 'Kerolos', 'year':21}
        }
print(myfamily) # {'child1': {'name': 'Kero', 'year': 21}, 'child2': {'name': 'Kerolos', 'year': 21}}

print(myfamily['child1']['name']) # Kero

myfamily['child1']['name'] = 'Mohamed'

print(myfamily['child1']['name']) # 'Mohamed'

print(myfamily) # {'child1': {'name': 'Mohamed', 'year': 21}, 'child2': {'name': 'Kerolos', 'year': 21}}

print("$" * 50)

child1 = {'name':'Kero', 'year':21}

child2 = {'name': 'Kerolos', 'year':21}

myfamily2 = {
        'child1' : child1,
        'child2' : child2
        }

print(myfamily) # {'child1': {'name': 'Kero', 'year': 21}, 'child2': {'name': 'Kerolos', 'year': 21}}

print(myfamily['child2']['year']) # 21

print("$" * 50)
