# counting to 20
for number in range(1, 21):
    print(number)

# Exercise 4-4: One Million

numbers = list(range(1, 1_000_001))

for number in numbers:
    print(number)

# Exercise 4-5: Summing a Million

numbers = list(range(1, 1_000_001))

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))

# Exercise 4-6: Odd Numbers

odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)

# Exercise 4-7: Threes

multiples_of_three = list(range(3, 31, 3))

for number in multiples_of_three:
    print(number)

# Exercise 4-8: Cubes

cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)

# Exercise 4-9: Cube Comprehension

cubes = [number ** 3 for number in range(1, 11)]

for cube in cubes:
    print(cube)
