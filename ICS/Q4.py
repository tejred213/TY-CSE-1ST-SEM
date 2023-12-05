#Write a program to check number is prime or not in Python

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        # Check odd factors up to the square root of num
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

# Example usage:
number = 19

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
