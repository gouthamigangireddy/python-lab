import csv

with open("payroll.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Basic Salary", "HRA", "DA", "Total Salary"])

    n = int(input("Enter number of employees: "))

    for i in range(n):
        name = input("Enter employee name: ")
        basic = float(input("Enter basic salary: "))

        hra = basic * 0.20
        da = basic * 0.10
        total = basic + hra + da

        writer.writerow([name, basic, hra, da, total])

print("\nPayroll Details:")

with open("payroll.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
