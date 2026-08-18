# Exercise 4-10: Slices

numbers = list(range(1, 11))

print("The first three items in the list are:")
print(numbers[:3])

print("Three items from the middle of the list are:")
print(numbers[3:6])

print("The last three items in the list are:")
print(numbers[-3:])

# Exercise 4-11: My Pizzas, Your Pizzas

pizzas = ["pepperoni", "margherita", "hawaiian"]

friend_pizzas = pizzas[:]

# Add a pizza to my list
pizzas.append("chicken")

# Add a different pizza to my friend's list
friend_pizzas.append("beef")

print("My favorite pizzas are:")

for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")

for pizza in friend_pizzas:
    print(pizza)

# Exercise 4-12: More Loops

foods = ["pizza", "burger", "rice", "chicken"]

for food in foods:
    print(food)

print()

foods_two = ["yam", "beans", "plantain", "fish"]

for food in foods_two:
    print(food)

