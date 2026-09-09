# Caesar Cipher

def caesar_encrypt(str1):

    shift = int(input("Enter the shift number : "))
    direction = input("Enter direction for shift : ").lower()

    cipher = ""

    if direction == "right":
        for i in range(len(str1)):
            curr = ord(str1[i])
            if 65 <= curr <= 90:
                new = (curr - 65 + shift) % 26 + 65     # Bring the char back to upper
            elif 97 <= curr <= 122:
                new = (curr - 97 + shift) % 26 + 97     # Bring the char back to lower
            else:
                new = curr
            new = chr(new)
            cipher += new

    else :
        for i in str1:
            curr = ord(i)
            if 65 <= curr <= 90:
                new = (curr - 65 - shift) % 26 + 65     # Bring the char back to upper
            elif 97 <= curr <= 122:
                new = (curr - 97 - shift) % 26 + 97     # Bring the char back to lower
            else:
                new = curr
            cipher += chr(new)
        
    return cipher

def caesar_decrypt(str1):

    shift = int(input("Enter the shift number : "))
    direction = input("Enter direction for shift : ").lower()

    cipher = ""

    if direction == "right":
        for i in range(len(str1)):
            curr = ord(str1[i])
            if 65 <= curr <= 90:
                new = (curr - 65 - shift) % 26 + 65     # Bring the char back to upper
            elif 97 <= curr <= 122:
                new = (curr - 97 - shift) % 26 + 97     # Bring the char back to lower
            else:
                new = curr
            new = chr(new)
            cipher += new

    else :
        for i in str1:
            curr = ord(i)
            if 65 <= curr <= 90:
                new = (curr - 65 + shift) % 26 + 65     # Bring the char back to upper
            elif 97 <= curr <= 122:
                new = (curr - 97 + shift) % 26 + 97     # Bring the char back to lower
            else:
                new = curr
            cipher += chr(new)
        
    return cipher

# Vigenere Cipher

def vigenere_encrypt(str1):

    key = input("Enter the key: ").upper()

    cipher = ""

    j = 0

    for i in range(len(str1)):

        curr = ord(str1[i])

        if 65 <= curr <= 90:
            k = ord(key[j % len(key)]) - 65
            new = (curr - 65 + k) % 26 + 65
            new = chr(new)
            cipher += new
            j += 1

        elif 97 <= curr <= 122:
            k = ord(key[j % len(key)]) - 65
            new = (curr - 97 + k) % 26 + 97
            new = chr(new)
            cipher += new
            j += 1
        else:
            new = chr(curr)
            cipher += new

    return cipher

def vigenere_decrypt(str1):

    key = input("Enter the key: ").upper()

    cipher = ""

    j = 0

    for i in range(len(str1)):

        curr = ord(str1[i])

        if 65 <= curr <= 90:
            k = ord(key[j % len(key)]) - 65
            new = (curr - 65 - k) % 26 + 65
            new = chr(new)
            cipher += new
            j += 1

        elif 97 <= curr <= 122:
            k = ord(key[j % len(key)]) - 65
            new = (curr - 97 - k) % 26 + 97
            new = chr(new)
            cipher += new
            j += 1
        else:
            new = chr(curr)
            cipher += new

    return cipher


while True:
    print("==== Cipher Menu ====")
    print("1. Caesar Cipher")
    print("2. Vigenere Cipher")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        text = input("Enter the text: ")
        option = input("Encrypt or Decrypt? (e/d): ").lower()
        if option == 'e':
            result = caesar_encrypt(text)
            print("Encrypted text:", result)
        elif option == 'd':
            result = caesar_decrypt(text)
            print("Decrypted text:", result)
        else:
            print("Invalid option")

    elif choice == 2:
        text = input("Enter the text: ")
        option = input("Encrypt or Decrypt? (e/d): ").lower()
        if option == 'e':
            result = vigenere_encrypt(text)
            print("Encrypted text:", result)
        elif option == 'd':
            result = vigenere_decrypt(text)
            print("Decrypted text:", result)
        else:
            print("Invalid option")

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")


