'''
Created on Dec 18, 2023

@author: apurs
'''

message = "Give me a number and I'll tell you if it's a multiple of ten."
message = int(input(message))

if message % 10 == 0:
    print(f"Yes, {message} is a multiple of ten!")
else:
    print(f"No, {message} is not a multiple of ten.")