'''
Created on Dec 14, 2023

@author: apurs
'''
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

print(favorite_languages['sarah'])

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
    
print("\n//////////////////////")

for name in favorite_languages.keys():
    print(name.title())
    
print("\n//////////////////////")
for name in favorite_languages:
    print(name.title())
    
    
friends = ['phil', 'sarah']

print("\n//////////////////////")
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
        
print("\n//////////////////////")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take out poll!")
    
print("\n//////////////////////")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
print("\n//////////////////////")
print('The following languages have been mentioned.')
for language in favorite_languages.values():
    print(language.title())
    
print("\n//////////////////////")
for language in set(favorite_languages.values()):
    print(language.title())
    
print("\n//////////////////////")
people_to_check = ['khala', 'brent', 'mallory', 'edward']

for people in favorite_languages.keys():
    if people in people_to_check:
        print(f"{people.title()}, Thank You for responding.")
    else:
        print(f"{people.title()}, Please take the poll.")
        
print("\n//////////////////////")
favorite_languages = {'jen':['python','rust'],
                      'sarah':['c'],
                      'edward':['rust','go'],
                      'phil':['python', 'haskell'],
                      }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite langguages are.")
    for language in languages:
        print(f"\t{language.title()}")
        
print("\n//////////////////////")      
        
    
    