'''
Created on Dec 4, 2023

@author: apurs
'''
#5-3
alien_color='green'

if alien_color=='green':
    print("+5 points")
    
alien_color='red'

if alien_color=='green':
    print("+5 points") 
    
#5-4
alien_color='green'

if alien_color=='green':
    print("+5 points")
else:
    print("+10 points")
    
alien_color='blue'

if alien_color=='green':
    print("+5 points")
else:
    print("+10 points")
    
#5-5
alien_color='red'

if alien_color=='green':
    print("+5 pionts")
    
elif alien_color=='yellow':
    print("+10 pionts")
    
elif alien_color=='red':
    print("+15 pionts")
        
#5-6
age=80

if age<2:
    print("\nThe person is a baby")
elif age>=2 and age<4:
    print("\nThe person is a toddler")     
elif age>=4 and age<13:
    print("\nThe person is a kid")
elif age>=13 and age<20:
    print("\nThe person is a teenager")
elif age>=20 and age<65:
    print("\nThe person is an adult")
else:
    print("\nThe person is an elder")
    
#5-7
favorite_fruits=['apple', 'orange', 'banana', 'grape']

if 'grape' in favorite_fruits:
    print("\nYou really like grapes")
    
if 'apple' in favorite_fruits:
    print("\nYou really like apple")
    
if 'orange' in favorite_fruits:
    print("\nYou really like orange")
    
if 'banana' in favorite_fruits:
    print("\nYou really like banana")