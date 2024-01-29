'''
Created on Dec 18, 2023

@author: apurs
'''

favorite_places = {'mike':['disney', 'paris', 'rohon', 'shire'], 'tim':['pinhurst'], 'bill':['westend', 'durham'], 'tom':[]}

for keys, values in favorite_places.items():
    print(f"{keys.title()}'s favorite places are....")
    
    if len(values) == 1:
        print(f"\t{values[0]}")
    else:
        index = len(values)
        str = ''
        for i in range(index):
            if i == 0:
                str = values[0].title()
            else:
                str = str + f", {values[i].title()}"
        print(f"\t{str}")