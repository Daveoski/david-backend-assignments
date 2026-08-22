person = {
    "first_name": "Orjionuchie",
    "last_name": "David",
    "age": 30,
    "city": "Portharcourt",
    "country": "Nigeria"
}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])
print(person["country"])

# favorite number
favorite_numbers = {
    "James": 7,
    "steph": 10,
    "David": 3,
    "seyi": 21,
    "lilian": 5
}

print("James's favorite number is " + str(favorite_numbers["James"]))
print("steph's favorite number is " + str(favorite_numbers["steph"]))
print("David's favorite number is " + str(favorite_numbers["David"]))
print("Seyi's favorite number is " + str(favorite_numbers["seyi"]))
print("lilian's favorite number is " + str(favorite_numbers["lilian"]))

# glossary
glossary = {
    "variable": "A name that stores a value.",
    "string": "A series of characters enclosed in quotation marks.",
    "list": "A collection of items stored in a specific order.",
    "loop": "A way to repeat a block of code.",
    "dictionary": "A collection of key-value pairs."
}

print("Variable:\n" + glossary["variable"] + "\n")
print("String:\n" + glossary["string"] + "\n")
print("List:\n" + glossary["list"] + "\n")
print("Loop:\n" + glossary["loop"] + "\n")
print("Dictionary:\n" + glossary["dictionary"])