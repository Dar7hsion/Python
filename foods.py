'''
Created on Oct 10, 2023

@author: apurs
'''
my_foods=['pizza','falafel','cake']
friend_foods=my_foods[:]
#this will point to the same list 
#friend_foods=my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("my favoite foods are.")
print(my_foods)

print("\nMy friends favorite foods are")
print(friend_foods)
print("\n")

my_foods=['pizza','falafel','cake']
friend_foods=my_foods
#this will point to the same list 
#friend_foods=my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("my favoite foods are.")
print(my_foods)

print("\nMy friends favorite foods are")
print(friend_foods)