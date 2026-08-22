person1 = {
    "first_name": "John",
    "last_name": "Smith",
    "age": 25,
    "city": "Lagos"
}

person2 = {
    "first_name": "Mary",
    "last_name": "Johnson",
    "age": 30,
    "city": "Abuja"
}

person3 = {
    "first_name": "David",
    "last_name": "Brown",
    "age": 22,
    "city": "Port Harcourt"
}

people = [person1, person2, person3]

for person in people:
    print("First name:", person["first_name"])
    print("Last name:", person["last_name"])
    print("Age:", person["age"])
    print("City:", person["city"])
    print()
    
    
    pet1 = {
    "animal": "dog",
    "owner": "John"
}

pet2 = {
    "animal": "cat",
    "owner": "Mary"
}

pet3 = {
    "animal": "parrot",
    "owner": "David"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("Animal:", pet["animal"])
    print("Owner:", pet["owner"])
    print()
    
    favorite_places = {
    "john": ["Lagos", "London", "Dubai"],
    "mary": ["Abuja", "Paris"],
    "david": ["Port Harcourt", "New York", "Tokyo"]
}

for person, places in favorite_places.items():
    print(person.title() + "'s favorite places are:")

    for place in places:
        print("- " + place)

    print()
    
    
    favorite_numbers = {
    "john": [7, 10, 21],
    "mary": [3, 8],
    "david": [5, 12, 20],
    "sarah": [4, 9],
    "james": [11, 15]
}

for person, numbers in favorite_numbers.items():
    print(person.title() + "'s favorite numbers are:")

    for number in numbers:
        print(number)

    print()
    
    cities = {
    "lagos": {
        "country": "Nigeria",
        "population": 15000000,
        "fact": "Lagos is one of the largest cities in Africa."
    },

    "london": {
        "country": "United Kingdom",
        "population": 9000000,
        "fact": "London is home to the famous Big Ben."
    },

    "tokyo": {
        "country": "Japan",
        "population": 14000000,
        "fact": "Tokyo is the capital of Japan."
    }
}

for city, information in cities.items():
    print("City:", city.title())
    print("Country:", information["country"])
    print("Population:", information["population"])
    print("Fact:", information["fact"])
    print()
    
    pet1 = {
    "name": "Max",
    "animal": "dog",
    "owner": "John",
    "age": 3,
    "color": "brown"
}

pet2 = {
    "name": "Luna",
    "animal": "cat",
    "owner": "Mary",
    "age": 2,
    "color": "white"
}

pet3 = {
    "name": "Coco",
    "animal": "parrot",
    "owner": "David",
    "age": 4,
    "color": "green"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("Pet name:", pet["name"])
    print("Animal:", pet["animal"])
    print("Owner:", pet["owner"])
    print("Age:", pet["age"])
    print("Color:", pet["color"])
    print()