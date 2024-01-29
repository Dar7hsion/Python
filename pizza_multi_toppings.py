'''
Created on Dec 29, 2023

@author: apurs
'''

# def make_pizza(*toppings):
#     """Print the list of toppings that have been reqquested."""
#     print(toppings)

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings.")
    for topping in toppings:
        print(f"-{topping}")



make_pizza(8, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')





