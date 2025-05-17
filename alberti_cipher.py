class AlbertiCipher:
    def __init__(self):
        self.outer_disk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Static outer disk (uppercase letters)
        self.inner_disk = 'abcdefghijklmnopqrstuvwxyz'  # Rotating inner disk (lowercase letters)
        self.disk_size = len(self.outer_disk)  # Number of characters (26)

    def rotate_inner_disk(self, shift):
        # Rotate the inner disk by the given shift value
        return self.inner_disk[shift:] + self.inner_disk[:shift]

    def encrypt(self, plaintext, initial_shift=0, rotation_frequency=2):
        """
        Encrypts the message using Alberti Cipher.
        - initial_shift: where the inner disk initially aligns with the outer disk (e.g., A = e if shift is 4)
        - rotation_frequency: how often the inner disk shifts during encryption
        """
        ciphertext = ''
        inner = self.rotate_inner_disk(initial_shift)  # Get the starting inner disk alignment
        count = 0  # Track number of alphabetic characters encrypted

        for char in plaintext.upper():
            if char in self.outer_disk:
                index = self.outer_disk.index(char)  # Find matching index in outer disk
                ciphertext += inner[index]  # Append mapped inner character
                count += 1
                # Rotate inner disk every N characters
                if count % rotation_frequency == 0:
                    inner = self.rotate_inner_disk((initial_shift + count) % self.disk_size)
            else:
                ciphertext += char  # Preserve non-alphabetic characters (spaces, punctuation, etc.)

        return ciphertext

    def decrypt(self, ciphertext, initial_shift=0, rotation_frequency=2):
        """
        Decrypts the message using Alberti Cipher.
        """
        plaintext = ''
        inner = self.rotate_inner_disk(initial_shift)  # Get the starting inner disk alignment
        count = 0  # Track number of alphabetic characters decrypted

        for char in ciphertext:
            if char in self.inner_disk:
                index = inner.index(char)  # Find matching index in current inner disk
                plaintext += self.outer_disk[index]  # Recover original uppercase character
                count += 1
                # Rotate inner disk every N characters
                if count % rotation_frequency == 0:
                    inner = self.rotate_inner_disk((initial_shift + count) % self.disk_size)
            else:
                plaintext += char  # Preserve non-alphabetic characters

        return plaintext

# Example usage
if __name__ == "__main__":
    cipher = AlbertiCipher()
    message = "CYBER BHUTAN"
    encrypted = cipher.encrypt(message, initial_shift=4, rotation_frequency=2)
    decrypted = cipher.decrypt(encrypted, initial_shift=4, rotation_frequency=2)

    print(f"Original Message:  {message}")
    print(f"Encrypted Message: {encrypted}")
    print(f"Decrypted Message: {decrypted}")
