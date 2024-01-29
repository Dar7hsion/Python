'''
Created on Oct 8, 2023

@author: apurs
'''
# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
# #changing a list
# motorcycles[0]='ducati'
# print(motorcycles)
# #Adding elements
# motorcycles.append('honda')
# print(motorcycles)
#
# motorcycles=[]
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)
# motorcycles.insert(0,'ducati')
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)
# del motorcycles[1]
# print(motorcycles)
#
#
# popped_motorcycle=motorcycles.pop()
# print(popped_motorcycle)

# motorcycles=['honda','yamaha','suzuki']
#
# last_owned=motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}")
# print(motorcycles)
# last_owned=motorcycles.pop(1)
# print(f"The last motorcycle I owned was a {last_owned.title()}")
# print(motorcycles)
#
# print(motorcycles.remove('honda'))

# motorcycles=['honda','yamaha','suzuki','ducati']
#
# print(motorcycles)
# too_expensive='ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")
#/////////////////////////////
invits=['alex','brent','chandler']
# print(f"{invits[0].title()}, please come to dinner.")
# print(f"{invits[1].title()}, please come to dinner.")
# print(f"{invits[2].title()}, please come to dinner.")
# #/////////////////////////////
# print(f"{invits[0].title()}, cant make it.")
# invits[0]='mallory'
# print(f"{invits[0].title()}, please come to dinner.")
# print(f"{invits[1].title()}, please come to dinner.")
# print(f"{invits[2].title()}, please come to dinner.")
#/////////////////////////////
print(f"{invits[0].title()}, {invits[1].title()}, {invits[2].title()}, I found a bigger table.")
invits.insert(0,'mallory')
invits.insert(2,'bill')
invits.append('tim')
print(f"{invits[0].title()}, please come to dinner.")
print(f"{invits[1].title()}, please come to dinner.")
print(f"{invits[2].title()}, please come to dinner.")
print(f"{invits[3].title()}, please come to dinner.")
print(f"{invits[4].title()}, please come to dinner.")
print(f"{invits[5].title()}, please come to dinner.")
#/////////////////////////////
print("Sadly we only have room for 2 poeple.")
print(f"{invits.pop()}, I have cancled your invtation.")
print(f"{invits.pop()}, I have cancled your invtation.")
print(f"{invits.pop()}, I have cancled your invtation.")
print(f"{invits.pop()}, I have cancled your invtation.")
print(f"{invits[0].title()}, please come to dinner.")
print(f"{invits[1].title()}, please come to dinner.")
del invits[0]
del invits[0]
print(invits)
