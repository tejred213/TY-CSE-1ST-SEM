#Write a program to find GCD of numbers a and b in Python
def prime_factors(num):
    factors = []
    divisor = 2

    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num = num // divisor
        divisor += 1

    return factors

def gcd_by_prime_factorization(a, b):
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)

    common_factors = set(factors_a) & set(factors_b)

    if common_factors:
        gcd_value = 1
        for factor in common_factors:
            gcd_value *= factor
        return gcd_value
    else:
        return 1  # If no common factors, GCD is 1

# Example usage:
num1 = 36
num2 = 48

result = gcd_by_prime_factorization(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
