'''
Created on Dec 17, 2023

@author: apurs
'''

rosie = {'name':'rosie', 'type':'dog', 'owner':{'first':'tim', 'last':'johns'}}
gizmo = {'name':'gizmo', 'type':'cat', 'owner':{'first':'ross', 'last':'blue'}}
doug = {'name':'doug', 'type':'dog', 'owner':{'first':'bill', 'last':'pike'}}

pets = [rosie, gizmo, doug]

for pet in pets:
    for key, value in pet.items():
        if key == 'name':
           print(f"Name: {value.title()}")
        elif key == 'type':
            print(f"Type: {value.title()}")
        else:
            str = 'Owner: '
            for k, v in value.items():
                str = str + f"{v.title()} "
            print(f"{str}\n")


#/////////////////////////////////////////////////////

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


#/////////////////////////////////////////////////////

def describle_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describle_pet('hamster', 'harry')
describle_pet('dog', 'willie')

#/////////////////////////////////////////////////////

def describle_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describle_pet(animal_type = 'hamster', pet_name = 'harry')
describle_pet(animal_type = 'dog', pet_name = 'willie')
describle_pet(pet_name = 'willie')

# A dog named Willie.
describle_pet('willie')
describle_pet(pet_name = 'willie')

# A hamster named Harry.
describle_pet('herry', 'hamster')
describle_pet(pet_name = 'herry', animal_type = 'hamster')
describle_pet(animal_type = 'hamster', pet_name = 'harry')

