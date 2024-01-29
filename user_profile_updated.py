'''
Created on Dec 29, 2023

@author: apurs
'''

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything 
    we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# user_profile = build_profile('albert', 'einstein', 
#                              location = 'princeton', 
#                              field = 'physics')

# print(user_profile)

user_profile = build_profile('alex', 'brooks', 
                             location = 'north carolina', 
                             field = 'computer sicence', 
                             hobby = 'game dev')

print(user_profile)

