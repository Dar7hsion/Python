'''
Created on Dec 18, 2023

@author: apurs
'''

cities = {'rohon':{'country':'middle earth', 'population':100000, 'fact':'lord of the rings'}, 
          'shire':{'country':'middle earth', 'population':100, 'fact':'lord of the rings again'}, 
          'hoth':{'country':'far far away', 'population':10, 'fact':'star wars'},
          }

for city, info in cities.items():
    print(f"City: {city.title()}")
    for k, v in info.items():
        print(f"{k.title()}: {v}")
        
        
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")


def describle_city(city, country='USA'):
    print(f"{city.title()} is in {country}")

describle_city('new york')
describle_city('cary')
describle_city('paris', 'franceq')


#//////////////////////////////////////////

def city_county(city, country):
    print(f"{city.title()}, {country.title()}")

city_county("santiago", "chile")
city_county("pinehurst", "USA")
city_county("new york", "new york")    