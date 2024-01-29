'''
Created on Dec 13, 2023

@author: apurs
'''
user_names = ['alex', 'brent', 'mallory', 'chandler', 'admin']

#usernames = [];

if user_names:
    for user in user_names:
        if user == 'admin':
            print(f"Hello {user}")
        else:
            print(f"{user}, thank you for logging in agin.")
            
else:
    print("We need to find some users!")          
      
########################################################

current_users = ['Alex', 'Brent', 'Mallory', 'Chandler', 'ADMIN']

new_users = ['alex', 'mallory', 'tim', 'tom', 'rick']

lower_case_users = []

for user in current_users:
    lower_case_users.append(user.lower())

for user in new_users:
    if user.lower() in lower_case_users:
        print("User name taken, please pick another user name.")
    else:
        print(f"User name {user} is available.")
        





