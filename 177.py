# 5-8. HELLO ADMIN
usernames = [
    "admin",
    "jaden",
    "sarah",
    "michael",
    "david"
]

for username in usernames:

    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

# 5-9. NO USERS
usernames = []

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

# 5-10. CHECKING USERNAMES
current_users = [
    "admin",
    "jaden",
    "sarah",
    "Michael",
    "David"
]

new_users = [
    "JOHN",
    "Jaden",
    "peter",
    "SARAH",
    "mike"
]

# Create a lowercase copy of current_users
current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

# Check each new username
for new_user in new_users:

    if new_user.lower() in current_users_lower:
        print(
            f"{new_user} is already taken. "
            "You will need to enter a new username."
        )
    else:
        print(f"{new_user} is available.")

# 5-11. ORDINAL NUMBERS
numbers = list(range(1, 10))

for number in numbers:

    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

