# Temperature Converter

print("TEMPERATURE CONVERTER")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice: ")
temperature = float(input("Enter temperature: "))

if choice == "1":
    result = (temperature * 9 / 5) + 32
    print("Temperature in Fahrenheit:", result)

elif choice == "2":
    result = (temperature - 32) * 5 / 9
    print("Temperature in Celsius:", result)

else:
    print("Invalid choice.")
