tom = {
    'name': 'tom',
    'kind': 'cat',
    'owner_name': 'guo jinfeng',
}

jerry = {
    'name': 'jerry',
    'kind': 'mouse',
    'owner_name': 'none'
}

wangcai = {
    'name': 'wangcai',
    'kind': 'dog',
    'owner_name': 'rick'
}

pets = [tom, jerry, wangcai]

for pet in pets:
    print("\nName: " + pet['name'].title())
    print("\tKind: " + pet['kind'])
    print("\tOwner's name: " + pet["owner_name"])
