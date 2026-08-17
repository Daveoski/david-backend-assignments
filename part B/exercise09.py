# list to string and back
words = ["Python", "is", "amazing"]

sentence = ", ".join(words)

print("List to String:", sentence)

new_list = sentence.split(", ")

print("String to List:", new_list)