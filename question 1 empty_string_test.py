# -------------------- EMPTY STRING TEST --------------------


print("----- EMPTY STRING TEST -----")

text = ""  # Define an empty string to test encryption/decryption
shift1 = 3  # First shift value for encryption
shift2 = 5  # Second shift value for encryption

# Call the encrypt_text function with the empty string and shift values.
# It returns the encrypted text and a log of the shifts applied.
encrypted, shift_log = encrypt_text(text, shift1, shift2)

# Print the encrypted result. Using repr() so an empty string is shown clearly as ''
print("Encrypted:", repr(encrypted))

# Print the log of shifts applied during encryption
print("Shift log:", shift_log)


# This should return the original text.
decrypted = decrypt_text(encrypted, shift_log)

# Print the decrypted text using repr() to make empty string visible
print("Decrypted:", repr(decrypted))

# Check if the decrypted text matches the original empty string
if decrypted == text:
    print("Test passed: Empty string encryption/decryption works!")
else:
    print("Test failed: Something went wrong.")