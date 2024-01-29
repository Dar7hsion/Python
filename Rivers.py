'''
Created on Dec 16, 2023

@author: apurs
'''

rivers = {'nile':'egypt', 'amazon':'south america', 'ob':'russia'}

for river, place in rivers.items():
    print(f"The {river} runs through {place}.")
    
for river in rivers.keys():
    print(river)
    
for place in rivers.values():
    print(place)   