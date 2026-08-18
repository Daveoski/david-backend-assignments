car = "subaru"

print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")


name = "Okechukwu"

print("\nIs name == 'Okechukwu'? I predict True.")
print(name == "Okechukwu")

print("\nIs name == 'David'? I predict False.")
print(name == "David")


age = 25

print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age == 30? I predict False.")
print(age == 30)


country = "Nigeria"

print("\nIs country != 'Ghana'? I predict True.")
print(country != "Ghana")

print("\nIs country != 'Nigeria'? I predict False.")
print(country != "Nigeria")


number = 10

print("\nIs number > 5? I predict True.")
print(number > 5)

print("\nIs number < 5? I predict False.")
print(number < 5)

# 5-2. MORE CONDITIONAL TESTS

fruit = "apple"

print("String equality:")
print(fruit == "apple")       # True
print(fruit == "banana")      # False

print("\nString inequality:")
print(fruit != "banana")      # True
print(fruit != "apple")       # False


name = "Okechukwu"

print("\nUsing lower():")
print(name.lower() == "okechukwu")  # True
print(name.lower() == "david")      # False


number = 10

print("\nNumerical equality:")
print(number == 10)    # True
print(number == 20)    # False

print("\nNumerical inequality:")
print(number != 20)    # True
print(number != 10)    # False

print("\nGreater than:")
print(number > 5)      # True
print(number > 20)     # False

print("\nLess than:")
print(number < 20)     # True
print(number < 5)      # False

print("\nGreater than or equal to:")
print(number >= 10)    # True
print(number >= 20)    # False

print("\nLess than or equal to:")
print(number <= 20)    # True
print(number <= 5)     # False

age = 25

print("\nUsing and:")
print(age >= 18 and age <= 30)   # True
print(age >= 30 and age <= 40)   # False


color = "red"

print("\nUsing or:")
print(color == "red" or color == "blue")      # True
print(color == "green" or color == "yellow")  # False

fruits = ["apple", "banana", "orange"]

print("\nItem in a list:")
print("banana" in fruits)     # True
print("mango" in fruits)      # False

print("\nItem not in a list:")
print("mango" not in fruits)  # True
print("banana" not in fruits) # False


alien_color = "green"

if alien_color == "green":
    print("The player just earned 5 points.")

alien_color = "red"

if alien_color == "green":
    print("The player just earned 5 points.")

# 5-4. ALIEN COLORS #2
alien_color = "green"

if alien_color == "green":
    print("The player just earned 5 points.")
else:
    print("The player just earned 10 points.")
alien_color = "yellow"

if alien_color == "green":
    print("The player just earned 5 points.")
else:
    print("The player just earned 10 points.")

# 5-5. ALIEN COLORS #3
alien_color = "green"

if alien_color == "green":
    print("The player earned 5 points.")
elif alien_color == "yellow":
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")

# 5-6. STAGES OF LIFE
age = 25
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")


# 5-7. FAVORITE FRUIT
favorite_fruits = ["mango", "banana", "orange"]

if "mango" in favorite_fruits:
    print("You really like mangoes!")

if "banana" in favorite_fruits:
    print("You really like bananas!")

if "orange" in favorite_fruits:
    print("You really like oranges!")

if "apple" in favorite_fruits:
    print("You really like apples!")

if "pineapple" in favorite_fruits:
    print("You really like pineapples!")

