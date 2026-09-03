# Prime Number and Factorial Program

num = int(input("Enter a positive number: "))

# Check Prime Number
if num < 2:
    print("The number is not prime.")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

# Find Factorial
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial of", num, "=", factorial)
