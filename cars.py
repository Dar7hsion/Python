'''
Created on Dec 4, 2023

@author: apurs
'''

cars = ['audi', 'bmw', 'subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())



#PS C:\Users\apurs> python
#Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> car='audi'
#>>> car=='bmw'
#False
#>>> car='Audi'
#>>> car=='audi'
#False
#>>> car='Audi'
#>>> car.lower()=='audi'
#True

class Car:
    """A simple attempt to model a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neeatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())