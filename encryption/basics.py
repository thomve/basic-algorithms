def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print(f"Encrypted (Caesar): {encrypted_text}")


def xor_cipher(text, key):
    return "".join(chr(ord(char) ^ key) for char in text)

text = "Hello, XOR!"
key = 7
encrypted_text = xor_cipher(text, key)
print(f"Encrypted (XOR): {encrypted_text}")
decrypted_text = xor_cipher(encrypted_text, key)
print(f"Decrypted (XOR): {decrypted_text}")


import hashlib

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Example usage
text = "Important message"
hashed_text = sha256_hash(text)
print(f"SHA-256 hash: {hashed_text}")
