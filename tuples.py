'''
Created on Oct 10, 2023

@author: apurs
'''
my_t=(3,)
dimensions=(200,50)

#cant be changed
#dimension[0]=250
#print(dimensions[0])
#print(dimensions[1])


print("Original dimensions.")
for dimension in dimensions:
    print(dimension)


dimensions=(400,100)    
print("\nModified dimensions.")
for dimension in dimensions:
    print(dimension)