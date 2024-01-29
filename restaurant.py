'''
Created on Jan 12, 2024

@author: apurs
'''

class Restaurant:
    """A simple attempt to model a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurants name is {self.restaurant_name} and they serve {self.cuisine_type}.")

    def open_restaurant(self):
        print("The restaurant is now open.")

steak = Restaurant('outback', 'Steak House')
steak.describe_restaurant()

mexican = Restaurant('la famila', 'mexican')
mexican.describe_restaurant()

subs = Restaurant('subway', 'sandwitchs')
subs.describe_restaurant()