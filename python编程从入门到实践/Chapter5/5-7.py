favorite_fruits = ['banana', 'apple', 'watermelon']
fruits = ['banana', 'apple', 'orange', 'watermelon', 'tomato']

if 'banana' in favorite_fruits:
    print('You really like banana.')
if 'apple' in favorite_fruits:
    print('You really like apples')
if 'orange' in favorite_fruits:
    print("You really like oranges.")
if 'watermelon' in favorite_fruits:
    print("You really like watermelons.")
if 'tomato' in favorite_fruits:
    print('You really like tomato.')

for fruit in fruits:
    if fruit in favorite_fruits:
        print('You really like {0}.'.format(fruit))
