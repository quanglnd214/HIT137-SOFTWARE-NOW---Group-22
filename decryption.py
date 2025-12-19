# decryption.py
# Reverses the encryption exactly

def decrypt_text(shift1, shift2):
    with open("encrypted_text.txt", "r") as file:
        text = file.read()

    decrypted = ""

    for char in text:
        # Lowercase letters
        if char.islower():
            if (ord(char) - 97 + (shift1 * shift2)) % 26 < 13:
                decrypted += chr((ord(char) - 97 - (shift1 * shift2)) % 26 + 97)
            else:  # n-z
                decrypted += chr((ord(char) - 97 + (shift1 + shift2)) % 26 + 97)

        # Uppercase letters
        elif char.isupper():
            if 'A' <= char <= 'M':
                decrypted += chr((ord(char) - 65 + shift1) % 26 + 65)
            else:  # N-Z
                decrypted += chr((ord(char) - 65 - (shift2 * shift2)) % 26 + 65)

        # Non-alphabet characters
        else:
            decrypted += char

    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted)
