# Student Grading Automation

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

total = maths + science + english
percentage = total / 3

print("\n===== STUDENT REPORT =====")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2))

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 35:
    grade = "E"
else:
    grade = "F"

print("Grade:", grade)

if percentage >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
