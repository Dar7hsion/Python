'''
Created on Oct 9, 2023

@author: apurs
'''
locations=['carthage','southern pines','pinehurst','aberdeen','vass']

print(locations)

print(sorted(locations))

print(locations)

print(sorted(locations, reverse=True))

print(locations)

#///////////////////////////

locations.reverse()

print(locations)

locations.reverse()

print(locations)

locations.sort()

print(locations)

locations.sort(reverse=True)

print(locations)

#///////////////////////////

print(len(locations))

#///////////////////////////

print("///////////////////////////\n")

things=['first','objects','tools','books','last']

print(things)
print(things[0])
print(things[0].title())
print(things[0].upper())
print(things[0].lower())
print(things[1])
print(things[3])
print(things[-1])

message=f"this will print last: {things[-1]}"
print(message)
things.append('crap')
print(things)

things.insert(0,'ball')
print(things)

del things[0]
print(things)

print(things.pop(0))
print(things)

things.remove('tools')
print(things)

print(sorted(things))
print(things)

print(sorted(things, reverse=True))
print(things)


things.sort()
print(things)

things.sort(reverse=True)
print(things)

things.reverse()
print(things)