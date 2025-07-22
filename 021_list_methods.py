# List Methods:

    # .count()
    # .index()
    # .reverse()

# .count() : count the specific things

list_of_numbers = [1, 2, 3, 9, 4, 5, 6, 7, 8, 9]

print(list_of_numbers) # [1, 2, 3, 9, 4, 5, 6, 7, 8, 9]

print("$" * 50)

print(list_of_numbers.count(9)) # 2

print("$" * 50)

counts = list_of_numbers.count(9)

print(counts) # 2

print("$" * 50)

list_of_names = ["Kerolos", "Mohamed", "Yousef", "Kerolos"]

print(list_of_names)

print("$" * 50)

print(list_of_names.count("Kerolos")) # 2

print("$" * 50)

print(list_of_names.count("kerolos")) # 0

print("$" * 50)



# .index() : searching for the value inside the list and return the number of the index

list_one = [1, 2, 3, 4, 5]

print(list_one.index(3)) # 2

print("$" * 50)

count_index = list_one.index(3)

print(count_index) # 2

print("$" * 50)

list_two = ["K", "M", "k", "m", "Y", "y"]

print(list_two.index("m")) # 3

print("$" * 50)

print(list_two.index("M")) # 1

print("$" * 50)


# .index(element, start_point, end_point)

list_three = [1, 2, 6, 3, 4, 5, 6, 7, 8, 9]

print(list_three.index(6)) # 2

print("$" * 50)

print(list_three.index(6, 3)) # 6

print("$" * 50)

print(list_three.index(6, 4, 8)) # 6



# .reverse() : reverse the list you give directly


print("$" * 50)

list_four = ["l", "m", "o", "p", "q", "a", "r"]

print(list_four) # ['l', 'm', 'o', 'p', 'q', 'a', 'r']

print("$" * 50)

# print(list_four.reverse()) # None => Empty 

list_four.reverse()

print(list_four) # ['r', 'a', 'q', 'p', 'o', 'm', 'l']

print("$" * 50)

list_five = [1, 2, 5, 3, 7, 9, 4]

print(list_five) # [1, 2, 5, 3, 7, 9, 4]

print("$" * 50)

list_five.reverse()

print(list_five) # [4, 9, 7, 3, 5, 2, 1]

print("$" * 50)

list_five.reverse()

print(list_five) # [1, 2, 5, 3, 7, 9, 4]





























