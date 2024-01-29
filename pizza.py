'''
Created on Dec 16, 2023

@author: apurs
'''

# #Store information about a pizza being ordered.

# pizza = {'crust':'thick',
#          'toppings':['mushrooms', 'extra cheese'],
#          }

# #Summarize the order
# print(f"You ordered a {pizza['crust']}-curst pizza "
#       "with the following toppings.")

# for topping in pizza['toppings']:
#     print(f"\t{topping}")

# toppings = []
# prompt = "\nAdd a topping."
# prompt += "\nWhen finished type 'quit'"

# while True:
#       top = input(prompt)      
#       if(top == 'quit'):
#             break

#       toppings.append(top)

#       print(f"\nWe've added {top} to your pizza.")

# print(f"\nHere is your requested toppings:")
# for each in toppings:
#      print(f"{each.title()}")

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch piza with the following toppings.")
    for topping in toppings:
        print(f"-{topping}")


        