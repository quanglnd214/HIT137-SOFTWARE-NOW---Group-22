"""
ASSIGNMENT 2
GROUP NAME: DAN/EXT 22
GROUP MEMBER:
Nguyen Duy Quang Lai        -   s389980
Angel Chang                 -   s377501
Nicole Suzanne Sattler      -   s195029
Youssef Elkassaby           -   s392402
============================================================================
Question 1
Create a program that reads the text file "raw_text.txt", encrypts its contents using a 
simple encryption method, and writes the encrypted text to a new file 
"encrypted_text.txt". Then create a function to decrypt the content and a function to 
verify the decryption was successful.
"""

def shift_char(char, shift):
    """
    Centralizes character shifting logic so encryption and decryption
    remain consistent and easy to reverse.
    """
    if char.islower():
        base = ord('a')
        # Calculate new position: (current_index + shift) % 26
        # This handles both positive (forward) and negative (backward) shifts automatically
        return chr((ord(char) - base + shift) % 26 + base)
    elif char.isupper():
        base = ord('A')
        # Same logic for uppercase letters
        return chr((ord(char) - base + shift) % 26 + base)
    
    # [cite_start]Return non-alphabetic characters unchanged [cite: 30]
    return char


def encrypt_text(text, shift1, shift2):
    """
    Applies assignment-specific encryption rules and records the exact
    shift used for each character so decryption can be guaranteed.
    """
    encrypted = []
    shift_log = []

    for ch in text:
        if ch.islower():
            # [cite_start]Rule for first half lowercase (a-m): Shift forward by shift1 * shift2 [cite: 25]
            if 'a' <= ch <= 'm':
                shift = shift1 * shift2
            # [cite_start]Rule for second half lowercase (n-z): Shift backward by shift1 + shift2 [cite: 26]
            else:
                shift = -(shift1 + shift2) # Negative indicates backward shift

            encrypted.append(shift_char(ch, shift))
            shift_log.append(shift)

        elif ch.isupper():
            # [cite_start]Rule for first half uppercase (A-M): Shift backward by shift1 [cite: 28]
            if 'A' <= ch <= 'M':
                shift = -shift1
            # [cite_start]Rule for second half uppercase (N-Z): Shift forward by shift2 squared [cite: 28]
            else:
                shift = shift2 ** 2

            encrypted.append(shift_char(ch, shift))
            shift_log.append(shift)

        else:
            # [cite_start]Special characters/numbers remain unchanged [cite: 30]
            encrypted.append(ch)
            shift_log.append(0) # 0 shift for non-alpha chars

    return ''.join(encrypted), shift_log


def decrypt_text(text, shift_log):
    """
    Reverses the encryption using the saved shift_log.
    This guarantees accuracy without needing complex reverse-logic.
    """
    decrypted = []

    # Create a list of opposite shifts (e.g., if we shifted +5, we now shift -5)
    reversed_shifts = [-s for s in shift_log]

    # Zip iterates through the encrypted text and the shift list simultaneously
    for ch, shift in zip(text, reversed_shifts):
        decrypted.append(shift_char(ch, shift))

    return ''.join(decrypted)


def encrypt_file(shift1, shift2):
    """
    Reads raw text, encrypts it, and saves both the result and the shift log.
    [cite_start]Corresponds to assignment Requirement[cite: 32].
    """
    try:
        # 'with' statement ensures file is properly closed after reading
        with open("raw_text.txt", "r", encoding="utf-8") as f:
            raw_text = f.read()

        # Perform the encryption logic
        encrypted, shift_log = encrypt_text(raw_text, shift1, shift2)

        # [cite_start]Write the encrypted content to file [cite: 19]
        with open("encrypted_text.txt", "w", encoding="utf-8") as f:
            f.write(encrypted)

        # Save the shift_log to a separate file so decrypt_file() can use it later
        with open("shift_log.txt", "w", encoding="utf-8") as f:
            f.write(",".join(map(str, shift_log)))
            
    except FileNotFoundError:
        print("Error: 'raw_text.txt' not found.")


def decrypt_file():
    """
    Reads the encrypted file and the helper log to reconstruct the original text.
    [cite_start]Corresponds to assignment Requirement[cite: 34].
    """
    try:
        with open("encrypted_text.txt", "r", encoding="utf-8") as f:
            encrypted_text = f.read()

        # Load the sequence of shifts used during encryption
        with open("shift_log.txt", "r", encoding="utf-8") as f:
            shift_log = list(map(int, f.read().split(",")))

        decrypted = decrypt_text(encrypted_text, shift_log)

        # Write the decrypted content to file
        with open("decrypted_text.txt", "w", encoding="utf-8") as f:
            f.write(decrypted)
            
    except FileNotFoundError:
        print("Error: Encrypted files not found.")


def verify_decryption():
    """
    Compares the original file with the decrypted file to prove they match.
    [cite_start]Corresponds to assignment Requirement[cite: 35].
    """
    try:
        with open("raw_text.txt", "r", encoding="utf-8") as f:
            original = f.read()

        with open("decrypted_text.txt", "r", encoding="utf-8") as f:
            decrypted = f.read()

        if original == decrypted:
            print("Decryption successful: files match.")
        else:
            print("Decryption failed: files do not match.")
            
    except FileNotFoundError:
        print("Error: Files for verification not found.")


def main():
    """
    Main driver function.
    [cite_start]Automatically prompts user, encrypts, decrypts, and verifies [cite: 36-41].
    """
    try:
        shift1 = int(input("Enter shift1: "))
        shift2 = int(input("Enter shift2: "))

        encrypt_file(shift1, shift2)
        decrypt_file()
        verify_decryption()
    except ValueError:
        print("Please enter valid integers for shifts.")


if __name__ == "__main__":

    main()
