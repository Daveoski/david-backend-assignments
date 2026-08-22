glossary = {
    "variable": "A name that stores a value.",
    "string": "A series of characters enclosed in quotation marks.",
    "list": "A collection of items stored in a specific order.",
    "loop": "A way to repeat a block of code.",
    "dictionary": "A collection of key-value pairs.",
    "function": "A block of code designed to perform a particular task.",
    "integer": "A whole number, such as 5 or 10.",
    "comment": "A note in a program that Python ignores.",
    "boolean": "A value that is either True or False.",
    "conditional": "A statement that allows a program to make decisions."
}

for word, meaning in glossary.items():
    print(word.title() + ":")
    print(meaning)
    print()
    
for word, meaning in glossary.items():
    print(word.title() + ":")
    print(meaning)
    print()


rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mississippi": "united states"
}

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("\nRivers:")

for river in rivers.keys():
    print(river.title())

print("\nCountries:")

for country in rivers.values():
    print(country.title())
    
    
    rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mississippi": "united states"
}

print("Rivers and the countries they run through:")

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("\nRivers:")

for river in rivers.keys():
    print(river.title())

print("\nCountries:")

for country in rivers.values():
    print(country.title())
    
    favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}
    
    people_to_poll = [
    "jen",
    "sarah",
    "mike",
    "john",
    "edward",
    "mary"
]
    
for person in people_to_poll:
    if person in favorite_languages:
        print("Thank you, " + person.title() + ", for responding to the poll!")
    else:
        print(person.title() + ", please take our favorite languages poll!")
        
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

people_to_poll = [
    "jen",
    "sarah",
    "mike",
    "john",
    "edward",
    "mary"
]

for person in people_to_poll:
    if person in favorite_languages:
        print("Thank you, " + person.title() + ", for responding to the poll!")
    else:
        print(person.title() + ", please take our favorite languages poll!")
        
