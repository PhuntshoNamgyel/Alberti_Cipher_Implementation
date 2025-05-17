from alberti_cipher import AlbertiCipher

def break_cipher(ciphertext, rotation_frequency=2):
    """
    Brute-force decryption attempts by trying all initial shifts (0 to 25).
    This assumes a constant rotation frequency.
    """
    results = []

    for shift in range(26):
        cipher = AlbertiCipher()
        plaintext = cipher.decrypt(ciphertext, initial_shift=shift, rotation_frequency=rotation_frequency)
        results.append((shift, plaintext))  # Store the result with its corresponding shift

    return results


if __name__ == "__main__":
    ciphertext = "gsiek vjkeda"  # Encrypted version of "CYBER BHUTAN" with shift=4, freq=2
    attempts = break_cipher(ciphertext, rotation_frequency=2)

    # Print all possible plaintexts to identify the correct one
    for shift, result in attempts:
        print(f"Initial Shift {shift}: {result}")
