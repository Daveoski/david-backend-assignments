# panlidrome
text = input("Enter a word or phrase: ")

cleaned_text = text.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
    print(f"{text} is a palindrome!")
else:
    print(f"{text} is not a palindrome.")