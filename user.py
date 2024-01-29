'''
Created on Dec 14, 2023

@author: apurs
'''
user_0 = {'username':'efermi', 
          'first':'enrico', 
          'last':'fermi'}

for key, value in user_0.items():
    print(f"\nKey:{key}")
    print(f"\nValue:{value}")

#///////////////////////////////////////
    
class User:
    """A simple attempt to model a User"""

    def __init__(self, first_name, last_name, age, password, user_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password
        self.user_name = user_name

    def describe_user(self):
        statment = f"Users name is {self.first_name} {self.last_name},"
        statment = statment + f"the users user name is {self.user_name},"
        statment = statment + f"there password is {self.password},"
        statment = statment + f" the user is {self.age} years old."
        print(statment)

    def greet_user(self):
        print(f"hello, {self.first_name} {self.last_name}.")


alex = User('Alex', 'Brooks', 31, 'password', 'abp22')

alex.describe_user()
alex.greet_user()