import random
import string


def generate_password():
    # Define the length of the password
    length = random.randint(9, 12)

    # Define the characters to use for the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    special_characters = string.punctuation

    # Create a list of all the possible characters
    possible_characters = list(uppercase_letters + lowercase_letters + special_characters)

    # Shuffle the list of possible characters
    random.shuffle(possible_characters)

    # Pick a random character from the list until the password is the desired length
    password = ''
    for i in range(length):
        password += random.choice(possible_characters)

    return password


print(generate_password())


























