def order_sandwiches(*toppings):
    print("\nThe toppings you want on the sandwiches are ")
    for topping in toppings:
        print(topping)


order_sandwiches('extra cheese', 'beef')
order_sandwiches('cheese', '')
