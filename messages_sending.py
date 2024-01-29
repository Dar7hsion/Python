'''
Created on Dec 27, 2023

@author: apurs
'''
messages = ["The cat is brown.", "The dog is white.", "The end is near."]
sent_messages = []

def show_messages(texts):
    for text in texts:
        print(text)

show_messages(messages)

def send_messages(texts):
    while texts:
        text = texts.pop()
        print(text)
        sent_messages.append(text)
    print(messages)
    print(sent_messages)

send_messages(messages[:])

print(messages)
print(sent_messages)

