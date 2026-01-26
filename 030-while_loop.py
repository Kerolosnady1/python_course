# while loop:

users = []

# condition = True

while(True):

    print("1.Add User\n2.Display\n3.Exit")

    choice = int(input("Enter a number: ").strip())

    if(choice == 1):
        user = input("Enter the user name: ").strip()
        users.append(user)
        print(f"{user} was added successfully!")

    elif (choice == 2):
        i = 0
        while(i < len(users)): # Ahmed Mohamed Kerolos
            print(users[i], end=" ")
            i += 1 # i = i + 1
        print()

    elif (choice == 3):
        print("Goodbye!")

        # condition = False

        break

    else:
        print("Invalid Choice!")
