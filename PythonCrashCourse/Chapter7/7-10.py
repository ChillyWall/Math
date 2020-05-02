resorts = {}
active = True
while active:
    name = input("What is your name? ")
    resort = input("If you could visit one place in the world, where would you go? ")
    repeat = input("Would you like to let another person response? (yes/ no)")

    resorts[name] = resort
    if repeat == 'no':
        active = False

for name, resort in resorts.items():
    print(name.title() + ' would like to visit ' + resort.title())