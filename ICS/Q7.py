#Write a program to check entered numbers are primitive root or not

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def is_primitive_root(g, p):
    if gcd(g, p) != 1:
        return False

    totient = euler_totient(p)

    for i in range(1, totient + 1):
        if pow(g, i, p) == 1:
            return False

    return True

# Get user inputs
base = int(input("Enter the base number: "))
modulo = int(input("Enter the modulo number: "))

# Check if the base is a primitive root modulo the modulo
if is_primitive_root(base, modulo):
    print(f"{base} is a primitive root modulo {modulo}.")
else:
    print(f"{base} is not a primitive root modulo {modulo}.")
