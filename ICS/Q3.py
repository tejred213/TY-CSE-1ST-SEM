#Write a program to calculate Euler totient function in Python
def euler_totient(n):
    result = n  # Initialize result as n

    # Check for all prime factors and apply Euler's totient formula
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    # If n has a prime factor greater than its square root
    if n > 1:
        result -= result // n

    return result

# Example usage:
num = 12
phi_value = euler_totient(num)
print(f"The Euler Totient Function of {num} is:", phi_value)
