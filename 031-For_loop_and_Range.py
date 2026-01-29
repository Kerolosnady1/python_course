# For Loop:
# What is the difference between while and for loop?

'''
while(True):
    print("Hello")
    ''' # Infinity loop


'''
names = ["Kerolos", "Mohamed", "Ahmed"]
for name in names:
    print(name, end=" ")

print()

for number in range(3):
    print(names[number], end=" ")
'''
'''
users = []

while True:

    print("1.Add User\n2.Display\n3.Exit")

    choice = int(input("Enter your choice: ").strip())


    if choice == 1:
        name = input("Enter a name: ").strip().capitalize()
        users.append(name)
        print(f"{name} was added successfully!")

    elif choice == 2:
        for name in users:
            print(name, end=" ")
        print()

    elif choice == 3:
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")

'''
'''
numbers = range(10)
print(numbers) # range(0, 10)
print(numbers[2]) # 2
print(numbers[:3]) # range(0, 3)

print(6 in numbers) # True

numbers = list(range(10))
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
