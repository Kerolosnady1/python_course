# .expandtabs()

name = "Kerolos\tNady"
print(name) # Kerolos Nady

msg = "Hello\tmy\tname\tis\tKero"
print(msg.expandtabs()) # Hello     my      name     is  Kero

msg2 = "Hello\tmy\tname\tis\tKero"
print(msg2.expandtabs(2)) # Hello  my  name  is  Kero


# .istitle()

msg3 = "I Love Python And 3G Technology"
print(msg3.istitle()) # True

msg4 = "i love python and 3g technology"
print(msg4.istitle()) # False

msg5 = "I love Python And 3G Technology"
print(msg5.istitle()) # False


# .isspace()

msg6 = "ilovepython"
print(msg6.isspace()) # False

msg7 = "i love python"
print(msg7.isspace()) # False

msg8 = " "
print(msg8.isspace()) # True

msg9 = ""
print(msg9.isspace()) # False


# .islower()

msg10 = "hello dear"
print(msg10.islower()) # True

msg11 = "Hello Dear"
print(msg11.islower()) # False

msg12 = "Hello dear"
print(msg12.islower()) # False



# .isidentifier()

varOne = "_Hello"
print(varOne.isidentifier()) # True

varTwo = "@file"
print(varTwo.isidentifier()) # False

varThree = "1Variable"
print(varThree.isidentifier()) # False

varFour = "V1ariable"
print(varFour.isidentifier()) # True

varFive = "Variable1"
print(varFive.isidentifier()) # True

varSix = "varFive"
print(varSix.isidentifier()) # True


# .replace()

msg13 = "Hello Sir"
print(msg13.replace("Hello", "Hi")) # Hi Sir

msg14 = "Hello Sir"
print(msg14.replace("H", "J")) # Jello Sir
