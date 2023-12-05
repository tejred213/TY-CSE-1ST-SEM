#Write a program to check numbers are co prime numbers or not in Python

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(num1, num2):
    return gcd(num1, num2) == 1

# Get user inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if the numbers are coprime
if are_coprime(num1, num2):
    print(f"{num1} and {num2} are coprime numbers.")
else:
    print(f"{num1} and {num2} are not coprime numbers.")
