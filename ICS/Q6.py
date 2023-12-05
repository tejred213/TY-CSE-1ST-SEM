#Write a program to find modular multiplicative inverse of A under modulo M (input A= 3 M=11)


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception(f"The modular inverse does not exist for {a} under modulo {m}")
    else:
        return x % m

# Example usage:
A = 3
M = 11

inverse_A = mod_inverse(A, M)
print(f"The modular multiplicative inverse of {A} under modulo {M} is:", inverse_A)
