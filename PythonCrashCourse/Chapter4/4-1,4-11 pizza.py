pizzas = ['type 1', 'type 2', 'type 3', 'type 4', 'type 5']
#print all the  pizzas' name
for pizza in pizzas:
    print('I like {0} pizza.'.format(pizza))
print("Pizza is one of my favorite food.")
print("I really love pizza.")


friend_pizzas = pizzas[:]

pizzas.append('type 6')
friend_pizzas.append('type 7')

print("My favorite pizzas are:", pizzas)
print("My friend's favorite pizzas are:", friend_pizzas)
