import random

while True:
    print("\n1. Roll Dice")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        number = random.randint(1, 6)
        print("Dice Result:", number)

    elif choice == "2":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
