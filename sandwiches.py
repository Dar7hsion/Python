'''
Created on Dec 29, 2023

@author: apurs
'''

def sandwich_orders(*order):
    """Prints each order based on user request"""
    print('Here is your order.')
    for item in order:
        print(f"-{item}")


sandwich_orders('pickles', 'cheese', 'mayo')

