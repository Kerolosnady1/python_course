# What is String?
# Access string with index
# Slicing
# Modify / methods

userName = "Kerolos"

msg = '''
Kerolos
Nady
'''
print(msg) # Kerolos \n # Nady

print(userName[0]) # K
print(userName[1]) # e
print(userName[-1]) # s

userNameUpdated = userName[0]
print(userNameUpdated) # K

userNameUpdated = 'S'
print(userNameUpdated) # S

print(userName[0:4]) # Kero => The end is not included

print(userName[0:]) # Kerolos
print(userName[:]) # Kerolos

print(userName[0:-1]) # Kerolo

print(userName[-6:-1]) # erolo

print(userName[-7:]) # Kerolos

print(userName[-6:]) # erolos

userNameUpdated = userName[0:4]
print(userNameUpdated) # Kero

integer1 = 10

'''str(userNameUpdated) = integer
print(userNameUpdated) # Error '''

integer2 = 20

integer1 = integer2

print(integer1) # 20
