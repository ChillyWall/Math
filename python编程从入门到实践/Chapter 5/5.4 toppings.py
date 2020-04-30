requested_toppings = ['mushrooms', 'green peppers','extra cheese']

for requested_topping in requested_toppings:
    print("Adding {0}.".format(requested_topping))

print("\nFinished making your pizza!")


print("-" * 30)


for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, wo are out of green peppers right now.")
    else:
        print("Adding {0}.".format(requested_toppings))


print("-" * 30)


requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding {0}.".format(requested_topping))
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


print('-' * 30)


available_toppings = ('mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese')
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in available_toppings:
    if requested_topping in requested_toppings:
        print("Adding {0}.".format(requested_topping))
    else:
        print("Sorry, we don't have {0}.".format(requested_topping))
print("\nFinished making your pizza.")


print('-' * 30)


