
def display_message(message):
    title: str = message.title()
    print(title)

display_message("i am happy to be learning python functions as David sat the front seat of the class")

def make_shirt(size, message):
    print(f"My T shirt is size {size} and has written the message: '{message}'.")


 # Positional arguments
make_shirt("Large", "I love Python")

 # Keyword arguments
make_shirt(size="Medium", message="Python is awesome")


def describe_city(city_name, city_state, city_population):
    print(f"The city {city_name} is located in {city_state} and has a population of {city_population}.")
describe_city("PH", "Obiakpor", "8,000,000")
describe_city("Lagos", "Bariga", "3,800,000")
describe_city("Enugu", "Abakpa", "2,700,000")


