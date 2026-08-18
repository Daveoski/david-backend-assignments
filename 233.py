# 7-8. DELI
sandwich_orders = [
    "tuna",
    "chicken",
    "pastrami",
    "egg",
    "beef"
]
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(sandwich)

# no pastrami
sandwich_orders = [
    "tuna",
    "pastrami",
    "chicken",
    "pastrami",
    "beef",
    "pastrami",
    "egg"
]

finished_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("\nRemaining sandwich orders:")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")

for sandwich in finished_sandwiches:
    print(sandwich)

# 7-10. DREAM VACATION
responses = {}

polling_active = True

while polling_active:

    name = input("\nWhat is your name? ")

    response = input(
        "If you could visit one place in the world, "
        "where would you go? "
    )

    responses[name] = response

    repeat = input(
        "\nWould you like to let another person respond? (yes/no) "
    )

    if repeat.lower() == "no":
        polling_active = False

print("\n--- Poll Results ---")

for name, place in responses.items():
    print(f"{name} would like to visit {place}.")

