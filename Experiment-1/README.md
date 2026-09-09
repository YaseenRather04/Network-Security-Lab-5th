# Experiment 1: Classical Symmetric Ciphers

## Aim

To implement and analyze Caesar Cipher and Vigenère Cipher in Python for encryption and decryption.

## Methodology

### Caesar Cipher

1. Take the plaintext, shift value, and shift direction as input.
2. Convert each character into its ASCII value.
3. Apply the shift using modulo 26.
4. Preserve uppercase and lowercase characters.
5. Preserve spaces and special characters.
6. Reverse the shift during decryption.

### Vigenère Cipher

1. Take the plaintext and key as input.
2. Convert each key character into a numerical shift.
3. Apply the repeating key to alphabetic characters.
4. Increment the key index only when an alphabetic character is processed.
5. Preserve spaces, special characters, and character case.
6. Add the key shift during encryption and subtract it during decryption.

## Features

- Menu-driven interface
- Caesar encryption and decryption
- Vigenère encryption and decryption
- User-defined shift and key
- Left and right Caesar shifts
- Case preservation
- Preservation of spaces and special characters
- Correct Vigenère key alignment

## Results

| Cipher | Encryption | Decryption | Verification |
|:------|:-----------|:-----------|:-------------|
| Caesar | Successful | Successful | Passed |
| Vigenère | Successful | Successful | Passed |

The decrypted text matched the original plaintext for the tested cases.

## Discussion

Caesar Cipher uses a fixed shift, making it easy to brute-force. Vigenère uses multiple shifts and provides better pattern concealment, but its repeating-key structure remains vulnerable.

## Improvements

- Added a menu-driven interface.
- Added runtime input for text, shift, direction, key, and operation.
- Added support for both left and right Caesar shifts.
- Preserved character case and special characters.
- Used a separate key index for correct Vigenère key alignment.

## Sample Output

### Caesar Cipher

```text
==== Cipher Menu ====
1. Caesar Cipher
2. Vigenere Cipher
3. Exit

Enter your choice: 1
Enter the text: Hello Network Security
Encrypt or Decrypt? (e/d): e
Enter the shift number: 3
Enter direction for shift: right

Encrypted text: Khoor Qhwzrun Vhfxulwb



