# Question1.py
from encryption import encrypt_text
from decryption import decrypt_text

def verify_decryption():
    with open("raw_text.txt", "r") as f1, open("decrypted_text.txt", "r") as f2:
        if f1.read() == f2.read():
            print("Decryption successful: files match.")
        else:
            print("Decryption failed: files do not match.")

def main():
    # Get numeric inputs safely (no try, assignment-safe)
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))

    encrypt_text(shift1, shift2)
    decrypt_text(shift1, shift2)
    verify_decryption()

if __name__ == "__main__":
    main()
