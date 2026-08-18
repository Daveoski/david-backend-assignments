# 7-4. PIZZA TOPPINGS
prompt = "Enter a pizza topping."
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)

    if topping.lower() == "quit":
        break

    print(f"I'll add {topping} to your pizza.")

# 7-5. MOVIE TICKETS
prompt = "Enter your age to find out the ticket price."
prompt += "\nEnter 'quit' when you are finished: "

while True:
    age = input(prompt)

    if age.lower() == "quit":
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

# 7-6 VERSION 1
# CONDITIONAL TEST IN THE WHILE STATEMENT
topping = ""

while topping.lower() != "quit":
    topping = input("Enter a pizza topping: ")

    if topping.lower() != "quit":
        print(f"I'll add {topping} to your pizza.")

# 7-6 VERSION 2
# ACTIVE VARIABLE
active = True

while active:
    topping = input("Enter a pizza topping: ")

    if topping.lower() == "quit":
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")

# 7-6 VERSION 3
# BREAK STATEMENT
while True:
    topping = input("Enter a pizza topping: ")

    if topping.lower() == "quit":
        break

    print(f"I'll add {topping} to your pizza.")

# 7-7. INFINITY
while True:
    print("This loop will never end!")

