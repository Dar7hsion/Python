'''
Created on Oct 9, 2023

@author: apurs
'''
squares=[]
for value in range(1,11):
    # square=value**2
    # squares.append(square)
    # or
    squares.append(value**2)
print(squares)

#or list comprehensions

squares_two=[value**2 for value in range(1,11)]
print(squares_two)