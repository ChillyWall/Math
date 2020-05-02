def make_pizza(size, *toppings):
    """Summarize the pizza wo are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following topping:")
    for topping in toppings:
        print("- " + topping)
