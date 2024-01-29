'''
Created on Dec 18, 2023

@author: apurs
'''

message = "How many people are in your dinning group?"
message = int(input(message))

if message > 8:
    print("You'll have to wait for a table.")
else:
    print("your table is ready.")