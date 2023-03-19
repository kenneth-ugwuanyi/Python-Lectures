import string

print("Paasword Checker Project")

print()


def password_checker():
    password = input("Input your password>>>>")
    min_length = 8
    special_character = string.punctuation
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase

    if len(password) < min_length:
        print("Password to short, password is a minimum of 8 characters")
        return False
    check_special_character = any(char in special_character for char in password)
    check_upper_case = any(char in upper_case for char in upper_case)
    check_lower_case = any(char in lower_case for char in lower_case)

    if not check_special_character:
        print("Invalid input your password must contain a special character")
        return False

    if not check_upper_case:
        print("Invalid input your password must contain at least one upper-case character")
        return False

    if not check_lower_case:
        print("Invalid input you password must contain a lower case character")
        return False

    else:
        print("Correct Format please hold while i validate your input")


print("Password Checker:\n")

print(password_checker())
