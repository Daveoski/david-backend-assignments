#Every Function

rivers = ["Nile", "Amazon", "Mississippi", "Niger", "Yangtze"]

# Print the original list
print("Original list:")
print(rivers)

# len()
print("\nNumber of rivers:")
print(len(rivers))

# append()
rivers.append("Congo")
print("\nAfter append():")
print(rivers)

# insert()
rivers.insert(2, "Danube")
print("\nAfter insert():")
print(rivers)

# remove()
rivers.remove("Mississippi")
print("\nAfter remove():")
print(rivers)

# pop()
removed_river = rivers.pop()
print("\nRiver removed using pop():")
print(removed_river)

print("List after pop():")
print(rivers)

# sorted()
print("\nAlphabetical order using sorted():")
print(sorted(rivers))

# reverse()
rivers.reverse()
print("\nAfter reverse():")
print(rivers)

# reverse() again
rivers.reverse()
print("\nAfter reverse() again:")
print(rivers)

# sort()
rivers.sort()
print("\nAfter sort():")
print(rivers)

# sort(reverse=True)
rivers.sort(reverse=True)
print("\nAfter sort(reverse=True):")
print(rivers)

# del
del rivers[0]
print("\nAfter del:")
print(rivers)