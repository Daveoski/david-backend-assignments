# city names
def city_country(city, country):
    return f"{city}, {country}"


print(city_country("Santiago", "Chile"))
print(city_country("Lagos", "Nigeria"))
print(city_country("London", "England"))

# album
def make_album(artiste, title, songs= None):
    album = {
        "artiste": artiste,
        "title": title,
        "song": songs
    }
    if songs:
        album["song"] = songs
    return album


album1 = make_album("Michael Jackson", "Thriller")
album2 = make_album("Wizkid", "Made in Lagos")
album3 = make_album("Davido", "Timeless")

print(album1)
print(album2)
print(album3)

# Album with number of songs
album4 = make_album("Burna Boy", "Love, Damini", 19)
print(album4)

def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if songs:
        album["songs"] = songs

    return album


while True:
    print("\nEnter album information:")
    print("Enter 'q' at any time to quit.")

    artist = input("Artist name: ")
    if artist == "q":
        break

    title = input("Album title: ")
    if title == "q":
        break

    album = make_album(artist, title)
    print(album)