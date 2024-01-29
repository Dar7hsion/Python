'''
Created on Dec 18, 2023

@author: apurs
'''

#message = input("Tell me something, and I will repeat it back to you:")
#message +="\nEnter 'quit' to end the program."

#print(message)

#name = input("Please enter your name:")
#print(f"\nHello, {name}")

#///////////////////////////////////////////

# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program."
#
# message = ""
#
# while message != 'quit':
#     message = input(prompt)
#
#     if message != 'quit':
#         print(message)
        
        
#///////////////////////////////////////////

prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."

active = True

while active:
    message = input(prompt)
    if message =='quit':
        active = False
    else:
        print(message)
        
#///////////////////////////////////////////
