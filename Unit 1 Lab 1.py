# Student Details and Grade

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

m1 = float(input("Enter marks in English: "))
m2 = float(input("Enter marks in Maths: "))
m3 = float(input("Enter marks in Science: "))

total = m1 + m2 + m3
percentage = total / 3

print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
elif percentage >= 35:
    print("Grade: D")
else:
    print("Result: Fail")
