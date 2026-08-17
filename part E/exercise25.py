# password strength
password = input("Enter your password: ")

has_number = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

if len(password) >= 8 and has_number and has_special:
    print("Password is strong.")
else:
    print("Password is weak.")
    print("It should contain at least 8 characters, one number, and one special character.")