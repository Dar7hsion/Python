'''
Created on Dec 14, 2023

@author: apurs
'''

alex_p = {'first_name':'alex', 'last_name':'powers', 'age':'31', 'city':'whispering place'}
tim_t = {'first_name':'tim', 'last_name':'thomas', 'age':'20', 'city':'high point'}
john_b = {'first_name':'john', 'last_name':'blue', 'age':'15', 'city':'yellow town'}

people = [alex_p, tim_t, john_b]

print(alex_p['first_name'])
print(alex_p['last_name'])
print(alex_p['age'])
print(alex_p['city'])
print('////////////////////\n')

favorite_numbers = {'alex':[22, 11], 'mallory':[2, 41], 'bill':[27, 51], 'tim':[28, 77], 'brent':[100, 13]}

print(f"alex {favorite_numbers['alex']}")
print(f"mallory {favorite_numbers['mallory']}")
print(f"bill {favorite_numbers['bill']}")
print(f"tim {favorite_numbers['tim']}")
print(f"brent {favorite_numbers['brent']}")

for names, numbers in favorite_numbers.items():
    print(f"{names.title()}'s favorite numbers are....")
    str = ''
    index = len(numbers)
    for i in range(index):
        if i == 0:
            str = f'{numbers[0]}'
        else:
            str = str + f", {numbers[i]}"
    print(f"\t{str}")


print('////////////////////\n')

for person in people:
    full_name = f"\tFull Name: {person['first_name'].title()} {person['last_name'].title()}"
    print(full_name)
    print(f"\tAge: {person['age']}")    
    print(f"\tCity: {person['city']}")    
    print('////////////////////')
    
    
    
    
    
