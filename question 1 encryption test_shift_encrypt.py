# -------------------- Encryption Code --------------------

def shift_char(char, shift):
    """
    Centralizes character shifting logic so encryption and decryption
    remain consistent and easy to reverse.
    """
    if char.islower():
        base = ord('a')
        return chr((ord(char) - base + shift) % 26 + base)
    elif char.isupper():
        base = ord('A')
        return chr((ord(char) - base + shift) % 26 + base)
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
            if 'a' <= ch <= 'm':
                shift = shift1 * shift2
            else:
                shift = -(shift1 + shift2)
            encrypted.append(shift_char(ch, shift))
            shift_log.append(shift)
        elif ch.isupper():
            if 'A' <= ch <= 'M':
                shift = -shift1
            else:
                shift = shift2 ** 2
            encrypted.append(shift_char(ch, shift))
            shift_log.append(shift)
        else:
            encrypted.append(ch)
            shift_log.append(0)
    return ''.join(encrypted), shift_log


def decrypt_text(text, shift_log):
    """
    Reverses the encryption using the saved shift_log.
    """
    decrypted = []
    reversed_shifts = [-s for s in shift_log]
    for ch, shift in zip(text, reversed_shifts):
        decrypted.append(shift_char(ch, shift))
    return ''.join(decrypted)


def encrypt_file(shift1, shift2):
    try:
        with open("raw_text.txt", "r", encoding="utf-8") as f:
            raw_text = f.read()
        encrypted, shift_log = encrypt_text(raw_text, shift1, shift2)
        with open("encrypted_text.txt", "w", encoding="utf-8") as f:
            f.write(encrypted)
        with open("shift_log.txt", "w", encoding="utf-8") as f:
            f.write(",".join(map(str, shift_log)))
    except FileNotFoundError:
        print("Error: 'raw_text.txt' not found.")


def decrypt_file():
    try:
        with open("encrypted_text.txt", "r", encoding="utf-8") as f:
            encrypted_text = f.read()
        with open("shift_log.txt", "r", encoding="utf-8") as f:
            shift_log = list(map(int, f.read().split(",")))
        decrypted = decrypt_text(encrypted_text, shift_log)
        with open("decrypted_text.txt", "w", encoding="utf-8") as f:
            f.write(decrypted)
    except FileNotFoundError:
        print("Error: Encrypted files not found.")


def verify_decryption():
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
    try:
        shift1 = int(input("Enter shift1: "))
        shift2 = int(input("Enter shift2: "))
        encrypt_file(shift1, shift2)
        decrypt_file()
        verify_decryption()
    except ValueError:
        print("Please enter valid integers for shifts.")


# -------------------- Test Code --------------------

def test_shift_char():
    print("Testing shift_char...")
    assert shift_char('a', 1) == 'b'
    assert shift_char('z', 1) == 'a'
    assert shift_char('a', -1) == 'z'
    assert shift_char('m', 26) == 'm'
    assert shift_char('n', -27) == 'm'
    assert shift_char('A', 1) == 'B'
    assert shift_char('Z', 1) == 'A'
    assert shift_char('A', -1) == 'Z'
    assert shift_char('1', 5) == '1'
    assert shift_char('!', 10) == '!'
    print("shift_char tests passed.\n")


def test_encrypt_decrypt_text():
    print("Testing encrypt_text and decrypt_text...")
    test_cases = [
        "",
        "abcdef",
        "nopqrst",
        "ABCDEF",
        "NOPQRST",
        "123!@#",
        "MixEd123!",
    ]
    shifts = [
        (1, 2),
        (3, 4),
        (0, 5),
        (-2, 3),
        (26, 52),
    ]
    for text in test_cases:
        for shift1, shift2 in shifts:
            encrypted, shift_log = encrypt_text(text, shift1, shift2)
            decrypted = decrypt_text(encrypted, shift_log)
            assert decrypted == text, f"Failed on '{text}' with shifts {shift1}, {shift2}"
    print("encrypt_text/decrypt_text tests passed.\n")


def test_boundaries():
    print("Testing alphabet boundary letters...")
    enc, log = encrypt_text("mn", 2, 3)
    dec = decrypt_text(enc, log)
    assert dec == "mn"
    enc, log = encrypt_text("MN", 2, 3)
    dec = decrypt_text(enc, log)
    assert dec == "MN"
    print("Boundary tests passed.\n")


if __name__ == "__main__":
    # Run tests instead of main program
    test_shift_char()
    test_encrypt_decrypt_text()
    test_boundaries()
    print("All tests passed successfully!")

    # Uncomment this line to run the interactive encryption program
    # main()
