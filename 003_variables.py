x = y = z = 5 # Assign multiple value to variable
print(x,y,z) # Print Multiple Variable value

names = ["Kerolos", "Mohamed", "Yousef"] # List => Array
nameOne, nameTwo, nameThree = names

print(nameOne, nameTwo, nameThree) # Kerolos Mohamed Yousef
print(names) # ['Kerolos', 'Mohamed', 'Yousef']

hpy = "Hello python"
print(hpy)

x, y = "Hello" , "python"
#   print(x,y) # Hello python # IndentationError

def func(): # indentation
    print("This is a function")
    var = 50
func() # Function calling # This is a function
print("Out of the function scope")

x, y = "Kerolos" , "Yousef" # from int(integer) => str(string)
print(x, y) # Kerolos Yousef

o , p = 60 , 80
print("o + p =",o + p) # o + p = 140

o , p = 60 , "k"
# print(o + p) # typeError

print( str(o) + p) # concatenate => 60k => convert from int into str
