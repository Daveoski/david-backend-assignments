guests = ["Charles", "Austino Melano", "Ifeanyi Iloka"]

print("Guest List")

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")


print("\nChanging Guest List")

print(f"Unfortunately, {guests[1]} can't make it to dinner.")

guests[1] = "stephanie Afunogu"

print("\nNew invitations:")

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")


print("\nMore Guests")

print("Good news! I found a bigger dinner table, so more guests can be invited.")

guests.insert(0, "ebuka Okoro")
guests.insert(2, "Loveth Eze")
guests.append("Mr Jonah")

print("\nNew invitations:")

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

print("\nShrinking Guest List")

print("Unfortunately, the new dinner table won't arrive in time.")
print("I can invite only two people for dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

print("\nThe following guests are still invited:")

for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

del guests[0]
del guests[0]

print("\nFinal guest list:")
print(guests)