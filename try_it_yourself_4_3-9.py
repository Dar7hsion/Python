'''
Created on Oct 9, 2023

@author: apurs
'''
for values in range(1,21):
    print(values)

odds=[]    
for odd_nums in range(1, 21, 2):
    odds.append(odd_nums)
print(odds)

threes=[]
for threes_nums in range(3, 31, 3):
    threes.append(threes_nums)
print(threes)

cube=[valus**3 for valus in range(1, 11)]
for values in cube:
    print(values)