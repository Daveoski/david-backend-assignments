def make_sandwich(*items):
    print("\nYour sandwich contains:")
    for item in items:
        print(f"- {item}")


make_sandwich("chicken", "cheese")

make_sandwich("beef", "lettuce", "tomato")

make_sandwich("tuna", "cheese", "lettuce", "tomato", "onions")


# user profile
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last

    return user_info


my_profile = build_profile(
    "Kosisochukwu",
    "Ojobasi",
    age=25,
    city="Enugu",
    profession="Programmer"
)

print(my_profile)


def make_car(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model

    return car_info


car = make_car(
    "subaru",
    "outback",
    color="blue",
    tow_package=True
)

print(car)


