def show_messages(messages):
    for message in messages:
        print(message)


messages = [
    "Hello!",
    "How are you?",
    "Python is fun!",
    "Keep learning!"
]

show_messages(messages)


# send a message
def send_messages(messages):
    sent_messages = []

    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

    return sent_messages


messages = [
    "Hello!",
    "How are you?",
    "Python is fun!",
    "Keep learning!"
]

sent_messages = send_messages(messages)

print("\nOriginal list:")
print(messages)

print("\nSent messages:")
print(sent_messages)


# archive message
def send_messages(messages):
    sent_messages = []

    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

    return sent_messages


messages = [
    "Hello!",
    "How are you doing?",
    "my Python is fun and easy to learn!",
    "Keep learning Daveoski!"
]

# Make a copy of the original list
messages_copy = messages[:]

sent_messages = send_messages(messages_copy)

print("\nOriginal list:")
print(messages)

print("\nSent messages:")
print(sent_messages)


