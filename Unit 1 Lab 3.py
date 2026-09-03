# Electricity Bill Calculator

name = input("Enter customer name: ")
units = float(input("Enter electricity units used: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)
else:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

print("\n----- ELECTRICITY BILL -----")
print("Customer:", name)
print("Units Used:", units)
print("Bill Amount: Rs.", bill)
