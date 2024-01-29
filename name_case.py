'''
Created on Oct 7, 2023

@author: apurs
'''
name="Eric"

print(f"Hello {name}, would you like to learn some Python today?")

#///////////////////////

first_name="alex"
last_name="purser"
full_name=f"{first_name} {last_name}"

print(full_name.upper())
print(full_name.lower())
print(full_name.title())

#///////////////////////

print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

#///////////////////////

famous_person='"A person who never made a mistake never tried anything new."'
message=f"Albert Einstein once said, {famous_person}"

print(message)

#///////////////////////
first_name="\talex\n"
last_name="\tpurser"
full_name=f"{first_name} {last_name}"
print(full_name)
full_name=f"{first_name.rstrip()} {last_name.rstrip()}"
print(full_name)
full_name=f"{first_name.lstrip()} {last_name.lstrip()}"
print(full_name)
full_name=f"{first_name.strip()} {last_name.strip()}"
print(full_name)

#///////////////////////

file='python_note.txt'

print(file.removesuffix('.txt'))