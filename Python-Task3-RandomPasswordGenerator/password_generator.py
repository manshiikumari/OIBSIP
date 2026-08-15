import random
import string

print("Random Password Generator")

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        print("\nChoose character types:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Numbers")
        print("4. Symbols")

        choices = input("Enter your choices (at least 2, e.g. 123): ")

        if len(set(choices)) < 2:
            print("Please select at least 2 character types.")
            continue

        characters = ""

        if "1" in choices:
            characters += string.ascii_uppercase

        if "2" in choices:
            characters += string.ascii_lowercase

        if "3" in choices:
            characters += string.digits

        if "4" in choices:
            characters += string.punctuation

        if not characters:
            print("Invalid choice. Please select from 1, 2, 3, or 4.")
            continue

        password = "".join(random.choice(characters) for _ in range(length))

        print("\nGenerated Password:", password)

        again = input("\nGenerate another password? (y/n): ")

        if again.lower() != "y":
            print("Thank you for using the Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number for the password length.")