my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

for food in my_foods:
    print(food)

print('-' * 30)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

for food in my_foods:
    print(food)
print('-' * 30)


print("The first three items in the list are:", my_foods[:3])
print("Three items in the middle of the list are:", my_foods[1:4])
print("The last three items in the list are:", my_foods[-3:])
print('-' * 30)


