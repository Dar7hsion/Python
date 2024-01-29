'''
Created on Dec 22, 2023

@author: apurs
'''
prompt = "Tickets are sold by age.\nWhat age are you?"
total = 0

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        if int(age) < 3:
            print(f"\nyour total is {total}.")
        elif int(age) >= 3 and int(age) <= 12:
            total = total + 10
            print(f"\nyour total is {total}.")
        else: 
            total = total + 15
            print(f"\nyour total is {total}.")
