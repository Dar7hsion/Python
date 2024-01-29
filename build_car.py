'''
Created on Dec 29, 2023

@author: apurs
'''

def make_car(brand, name, **info):
    info['brand_name'] = brand
    info['car_name'] = name
    return info

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)

print(car)




