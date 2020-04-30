cities = {
    'beijing': {
        'country': 'china',
        'population': 20000000,
        'fact': "It's the capital of China"
    },
    'new york': {
        'country': 'america',
        'population': 9000000,
        'fact': "It'sthe capital of America"
    },
    'london': {
        'country': 'england',
        'population': 7000000,
        'fact': "It's the capital of England"
    },
}
for city, info in cities.items():
    print("\nName: " + city)
    print("The country it stands is {0}"
          .format(info['country'].title()))
    print("The population of it is {0}"
          .format(info['population']))
    print("About it there is a fact that {0}"
          .format(info['fact']))
