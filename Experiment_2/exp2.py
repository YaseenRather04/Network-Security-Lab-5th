from hashlib import sha256


def hash_text(plain_text):
    hash_value = sha256(plain_text.encode()).hexdigest()
    return hash_value


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    return data


def hash_file(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
    return sha256(data).hexdigest()


def tampering_simulation(file_path):
    data = read_file(file_path)

    print("\nCurrent file content:")
    print(data)

    print("\nWhat do you want to simulate?")
    print("1. Update an existing word")
    print("2. Append text")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        old_word = input("Enter the word to replace: ").strip()
        new_word = input("Enter the new word: ").strip()

        if old_word not in data:
            print("The word was not found in the file.")
            return

        updated_data = data.replace(old_word, new_word)

    elif choice == "2":
        new_text = input("Enter the text to append: ")

        if data and not data.endswith((" ", "\n", "\t")):
            new_text = " " + new_text

        updated_data = data + new_text

    else:
        print("Invalid choice. Please select 1 or 2.")
        return

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_data)

    print("\nUpdated file content:")
    print(updated_data)
    print("New hash:", hash_file(file_path))


while True:
    print("\nMenu")
    print("1. Hash typed text")
    print("2. Hash a file")
    print("3. Tampering simulation")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        text = input("Enter the text you want to hash: ")
        print("Hash value:", hash_text(text))

    elif choice == "2":
        file_path = input("Enter file name if in same folder or full path: ")
        try:
            print("Hash value:", hash_file(file_path))
            print(read_file(file_path))
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")

    elif choice == "3":
        file_path = input("Enter file name if in same folder or full path: ")
        try:
            tampering_simulation(file_path)
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

