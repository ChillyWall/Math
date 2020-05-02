favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title())
print(favorite_languages['sarah'].title())

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite languages is " +
          language.title())

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi {0}, I see your favorite languages is {1}!"
              .format(name.title(), favorite_languages[name]
                      .title()))

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())

questioned_people = ['bryce', 'juli', 'pasty', 'rick', 'edward'
                     'phil', 'jen', 'sarah']
for person in questioned_people:
    if person in favorite_languages.keys():
        print(person.title() + ", thank you for being questioned.")
    else:
        print(person.title() + ", we'd like to invite you to be questioned.")


# 6.4.2
favorite_languages_2 = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages_2.items():
    if len(languages) >= 2:
        print("\n" + name.title() + "'s favorite languages are: ")
        for language in languages:
            print("\t" + language.title())
    elif len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is " +
              languages[0].title() + ".")
