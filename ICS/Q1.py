# Implementation ot Caesar Cypher in Python/C++/Java

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char

    return result

# Example usage:
plaintext = "Hello, World!"
shift_value = 3
encrypted_text = caesar_cipher(plaintext, shift_value)
print("Original Text:", plaintext)
print("Encrypted Text:", encrypted_text)

# Decrypting the text
decrypted_text = caesar_cipher(encrypted_text, -shift_value)
print("Decrypted Text:", decrypted_text)
