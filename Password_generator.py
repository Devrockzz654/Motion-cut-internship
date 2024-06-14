import random
import string

def generate_password():
    # Prompt the user for password length and complexity preferences
    password_length = int(input("Enter the desired password length: "))
    password_complexity = {}
    while True:
        password_complexity['lowercase'] = input("Include lowercase letters? (y/n): ").lower() in ('y', 'yes')
        password_complexity['uppercase'] = input("Include uppercase letters? (y/n): ").lower() in ('y', 'yes')
        password_complexity['numbers'] = input("Include numbers? (y/n): ").lower() in ('y', 'yes')
        password_complexity['symbols'] = input("Include symbols? (y/n): ").lower() in ('y', 'yes')
        if any(password_complexity.values()):
            break
        else:
            print("Please ensure that you have selected at least one character type.")

    password_characters = ''
    if password_complexity['lowercase']:
        password_characters += string.ascii_lowercase
    if password_complexity['uppercase']:
        password_characters += string.ascii_uppercase
    if password_complexity['numbers']:
        password_characters += string.digits
    if password_complexity['symbols']:
        password_characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(password_characters) for _ in range(password_length))

    # Display the generated password
    print("Your generated password is:\n" + password)

# Generate and display the password
generate_password()
