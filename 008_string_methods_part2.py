# .upper()

name = "kerolos"
print(name) # kerolos
print(name.upper()) # KEROLOS

msg = "Hello, my name is Kerolos"
print(msg.upper()) # HELLO, MY NA,E IS KEROLOS


# .lower()

userName = "Mohamed"
print(userName.lower()) # mohamed

msg2 = "HELLO, MY NAME IS MOHAMED"
print(msg2.lower()) # hello, my name is mohamed

# .split()

name = "Kerolos Nady"
print(name.split()) # ['Kerolos', 'Nady']

name2 = "MohamedAhmed"
print(name2.split()) # ['MohamedAhmed']

name3 = "Yousef,Mohamed"
print(name3.split(",")) # ['Yousef', 'Mohamed']

name4 = "Omar#Ahmed"
print(name4.split("#")) # ['Omar', 'Ahmed']

name5 = "Yas#sinMohamed"
print(name5.split("#")) # ['Yas', 'sinMohamed']

msg3 = "Hello, my name is Kerolos"
print(msg3.split()) # ['Hello,', 'my', 'name', 'is', 'Kerolos']

msg4 = "Hello, dear How are you?"
print(msg4.split(" ", 3)) # ['Hello,', 'dear', 'How', 'are you?']

# .rsplit()

name6 = "Kerolos Nady Gerges"
print(name6.rsplit()) # ['Kerolos Nady', 'Gerges']

name7 = "Kerolos,Nady,Hello,Gerges,Farag"
print(name7.rsplit(",", 3)) # ['Kerolos,Nady', 'Hello', 'Gerges', 'Farag']


# .count()

msg5 = "I love python"
print(msg5.count("o")) # 2

msg6 = "I love python and python is a programming language"
print(msg6.count("python")) # 2


# .swapcase()

msg7 = "Hello, My Name Is Kerolos"
print(msg7.swapcase()) # hELLO, mY nAME iS kEROLOS


# .capitalize()

msg8 = "hello, my name is Kerolos"
print(msg8.capitalize()) # Hello, my name is kerolos


# .startswith()

msg9 = "I love python"
print(msg9.startswith("I")) # True

msg10 = "I love python"
print(msg10.startswith("w")) # False


# .endswith()

msg11 = "Hello, my name is Kerolos"
print(msg11.endswith("s")) # True

msg12 = "Hello, my name is Kerolos"
print(msg12.endswith("m")) # False


# .find()

msg13 = "I love python very much"
print(msg13.find("very")) # 14

msg14 = "I love python very much"
print(msg14.find("p")) # 7
