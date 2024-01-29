'''
Created on Dec 22, 2023

@author: apurs
'''

polls = {}
polling_active = True

while polling_active:
    name = input("Whats your name?")
    response = input("If you could visit one place in the world, whare would you go?")

    #Store the response in the dictionary.
    polls[name] = response

    #Fin out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person resond? (yes/no)")

    if repeat == 'no':
        polling_active = False

print("\n---Poll Results---")
for name, response in polls.items():
    print(f"{name} would like to go {response}.")



