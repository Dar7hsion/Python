'''
Created on Dec 22, 2023

@author: apurs
'''

sandwich_orders = ['sub','pastrami', 'pb&j', 'griled_cheese', 'pastrami', 'pastrami']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        print("The deli has run out of pastrami.")
        continue
    print(f"I have made you {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("sandwiches Made:")
for each in finished_sandwiches:
    print(each)


