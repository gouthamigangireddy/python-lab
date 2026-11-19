import csv
import matplotlib.pyplot as plt

data = [
    ["Product", "Sales"],
    ["Laptop", 50000],
    ["Mobile", 30000],
    ["Tablet", 20000],
    ["Headphones", 10000],
    ["Keyboard", 5000]
]

with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

products = []
sales = []

with open("sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        products.append(row[0])
        sales.append(int(row[1]))

print("RETAIL SALES REPORT")
print("-------------------")

total = sum(sales)
average = total / len(sales)

print("Total Sales:", total)
print("Average Sales:", average)
print("Highest Sales:", max(sales))

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(products, sales)
plt.title("Retail Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Sales Amount")
plt.show()

# Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(sales, labels=products, autopct="%1.1f%%")
plt.title("Product Sales Percentage")
plt.show()