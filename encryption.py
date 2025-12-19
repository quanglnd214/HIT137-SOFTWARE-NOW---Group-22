# encryption.py
# Handles text encryption based on assignment rules

def encrypt_text(shift1, shift2):
    with open("raw_text.txt", "r") as file:
        text = file.read()

    encrypted = ""

    for char in text:
        # Lowercase letters
        if char.islower():
            if (ord(char) - 97 + (shift1 * shift2)) % 26 < 13:
                encrypted += chr((ord(char) - 97 + (shift1 * shift2)) % 26 + 97)
            else:  # n-z
                encrypted += chr((ord(char) - 97 - (shift1 + shift2)) % 26 + 97)

        # Uppercase letters
        elif char.isupper():
            if 'A' <= char <= 'M':
                encrypted += chr((ord(char) - 65 - shift1) % 26 + 65)
            else:  # N-Z
                encrypted += chr((ord(char) - 65 + (shift2 * shift2)) % 26 + 65)

        # Non-alphabet characters
        else:
            encrypted += char

    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted)
