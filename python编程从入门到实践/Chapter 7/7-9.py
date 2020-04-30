sandwich_orders = ['pastrami', 'Stoner’s Delight', 'pastrami', 'A Wreck',
                   'Something Else', 'pastrami']
finished_sandwiches = []
print("We are sorry, there is lack of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    print("I made you tuna sandwich.")

    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)