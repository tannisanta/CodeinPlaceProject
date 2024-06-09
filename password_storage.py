import string
import secrets


# Function to generate a password based on the parameters specified by user
def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    characters = ''
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    # Generate password using secrets module
    # https://docs.python.org/3/library/secrets.html
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


# Function to save the password and keyword to a file
def save_to_file(keyword, password, filename):
    existing_keywords = get_existing_keywords(filename)
    if keyword in existing_keywords:
        print(f"The keyword '{keyword}' is already in use. Please choose a different keyword.")
        return

    with open(filename, 'a') as file:
        file.write(f"{keyword}: {password}\n")


# Function to retrieve passwords from the file based on the provided keyword
def retrieve_from_file(filename, keyword=None):
    passwords_found = False
    with open(filename, 'r') as file:
        for line in file:
            if ':' in line:
                key, pw = line.strip().split(':', 1)
                if keyword is None or key == keyword:
                    print(f"Keyword: {key}, Password: {pw}")
                    passwords_found = True

    if not passwords_found:
        print("No passwords found. Add a password.")


# Function to get a list of existing keywords from the file
def get_existing_keywords(filename):
    existing_keywords = []
    with open(filename, 'r') as file:
        for line in file:
            if ':' in line:
                key, _ = line.strip().split(':', 1)
                existing_keywords.append(key)
    return existing_keywords


# Function to count the number of passwords stored in the file
def count_passwords(filename):
    num_passwords = 0
    with open(filename, 'r') as file:
        for line in file:
            num_passwords += 1
    print(f"You now have {num_passwords} passwords stored.")


# Main function to manage password operations
def main():
    filename = "passwords.txt"

    while True:
        user_input = input("Do you want to add a password, view a specific password, view all passwords? add/view/view all/exit: ").lower()

        print("")

        if user_input == 'add':
            # Prompt the user for password generation parameters
            length = int(input("Enter the desired password length: "))
            include_uppercase = input("Include uppercase letters? y/n: ").lower() == 'y'
            include_lowercase = input("Include lowercase letters? y/n: ").lower() == 'y'
            include_numbers = input("Include numbers? y/n: ").lower() == 'y'
            include_symbols = input("Include symbols? y/n: ").lower() == 'y'
            print("")

            # Generate the password based on the user responses
            password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
            print(f"Your generated password is: {password}")
            print("")

            # Prompt the user for a keyword and validate that it is not already on the list
            while True:
                keyword = input("Enter a keyword to store the password: ")
                if keyword in get_existing_keywords(filename):
                    print(f"The keyword '{keyword}' is already in use. Please choose a different keyword.")
                else:
                    break

            print("")

            # Save the password and keyword to the file
            save_to_file(keyword, password, filename)
            print(f"Success! The password has been saved with the keyword '{keyword}'.")
            count_passwords(filename)

        elif user_input == 'view':
            # Prompt the user for a keyword to view the corresponding password
            keyword = input("Enter the keyword to view the password (leave blank to view all): ").strip()
            retrieve_from_file(filename, keyword if keyword else None)

        elif user_input == 'view all':
            # Retrieve and display all stored passwords
            retrieve_from_file(filename)
            print("")
            user_input = input("Do you want to exit? y/n: ")
            if user_input == 'y':
                print("Mission accomplished! See you next time.")
                break

        elif user_input == 'exit':
            print("Mission accomplished! See you next time.")
            break

        else:
            print("Invalid input. Please enter 'add', 'view', 'view all', or 'exit'.")

        print("")


if __name__ == "__main__":
    main()
    