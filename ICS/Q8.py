#Write a program to find GCD of number using Euclid algorithm in Python

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Get user inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD using the Euclidean algorithm
result = gcd(num1, num2)

# Print the result
print(f"The GCD of {num1} and {num2} is:", result)
