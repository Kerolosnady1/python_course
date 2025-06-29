# String Methods => built-in functions

# len(variable_name)
userName = "Kerolos Nady"
print(len(userName)) # 12

print(userName[len(userName) - 1]) # y => 12 - 1 = 11
print(userName[len(userName) - 2]) # d => 12 - 2 = 10

print(userName[-1]) # y
print(userName[-2]) # d

# .strip()
userName = " Kerolos "
print(userName) #  Kerolos
print(userName.strip()) # Kerolos

userName = "@#Kerolos@#"
print(userName) # @#Kerolos@#
print(userName.strip("@#")) # Kerolos
print(userName.strip()) # @#Kerolos@#

# .rstrip()
userName = " Kerolos "
print(userName) #  Kerolos 
print(userName.rstrip()) #  Kerolos

userName = "#Kerolos#"
print(userName) # #Kerolos#
print(userName.rstrip("#")) # #Kerolos

# .lstrip()
userName = " Kerolos "
print(userName) #  Kerolos 
print(userName.lstrip()) # Kerolos

userName = "#Kerolos#"
print(userName) # #Kerolos#
print(userName.lstrip("#")) # Kerolos#

# .title()
msg = "i love python and 5g technology"
print(msg) # i love python and 5g technology
print(msg.title()) # I Love Python And 5G Technology
