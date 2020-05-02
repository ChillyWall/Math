sandwich_orders = ['Stoner’s Delight', 'A Wreck', 'Something Else']
finished_sandwiches = []
while sandwich_orders:
    print("I made you tuna sandwich.")

    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)