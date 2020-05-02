prompt = "Please tell me your age: "
while True:
    age = int(input(prompt))
    if age < 3:
        print("The cost is free,")
    elif age < 12:
        print("The cost is 10$.")
    else:
        print("The cost is 15$.")
