while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")

        file = open("students.txt", "a")
        file.write(name + "," + roll + "," + marks + "\n")
        file.close()

        print("Student added successfully!")

    elif choice == "2":
        file = open("students.txt", "r")

        print("\nStudent Details:")

        for line in file:
            print(line.strip())

        file.close()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")