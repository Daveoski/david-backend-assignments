# addition calculator
while True:
    print("\nEnter two numbers.")
    print("Enter 'q' to quit.")

    first_number = input("First number: ")

    if first_number == "q":
        break

    second_number = input("Second number: ")

    if second_number == "q":
        break

    try:
        answer = int(first_number) + int(second_number)
        print(f"The answer is: {answer}")

    except ValueError:
        print("Sorry, please enter valid numbers.")
        

# add
try:
    first_number = input("Enter the first number: ")
    first_number = int(first_number)

    second_number = input("Enter the second number: ")
    second_number = int(second_number)

    answer = first_number + second_number

    print(f"The answer is: {answer}")

except ValueError:
    print("Sorry, please enter numbers only.")
    
# cat and dog
filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename, encoding="utf-8") as file:
            contents = file.read()
            print(f"\nContents of {filename}:")
            print(contents)

    except FileNotFoundError:
        print(f"\nSorry, the file '{filename}' was not found.")
        
        
# silent cat and dog
filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename, encoding="utf-8") as file:
            contents = file.read()
            print(f"\nContents of {filename}:")
            print(contents)

    except FileNotFoundError:
        pass
    
    
# common word
filenames = ["alice.txt", "frankenstein.txt"]

for filename in filenames:
    try:
        with open(filename, encoding="utf-8") as file:
            contents = file.read()

            the_count = contents.lower().count("the")
            the_space_count = contents.lower().count("the ")

            print(f"\nFile: {filename}")
            print(f"'the' appears approximately {the_count} times.")
            print(f"'the ' appears approximately {the_space_count} times.")

    except FileNotFoundError:
        print(f"Sorry, {filename} was not found.")