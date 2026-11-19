students = {}

while True:
    print("\n--- Attendance Tracker ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        students[name] = {"present": 0, "total": 0}

        print("Student added successfully!")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            status = input("Enter P for Present or A for Absent: ").upper()

            students[name]["total"] += 1

            if status == "P":
                students[name]["present"] += 1

            print("Attendance marked!")

        else:
            print("Student not found!")

    elif choice == "3":
        print("\n--- Attendance Report ---")

        for name, data in students.items():
            total = data["total"]
            present = data["present"]

            if total > 0:
                percentage = (present / total) * 100
            else:
                percentage = 0

            print("Name:", name)
            print("Present:", present)
            print("Total Classes:", total)
            print("Attendance:", round(percentage, 2), "%")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")