prompt = "Please tell me your age: "


# 方法1
prompt = "(1)" + prompt
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        age = int(message)
        if age < 3:
            print("The cost is free,")
        elif age < 12:
            print("The cost is 10$.")
        else:
            print("The cost is 15$.")


# 方法2
prompt = "(2)" + prompt
active = True
while active:
    message = input(prompt)
    if message != 'quit':
        age = int(message)
        if age < 3:
            print("The cost is free.")
        elif age < 12:
            print("The cost is 10$.")
        else:
            print("The cost is 15$.")
    else:
        active = False

# 方法3
prompt = "(3)" + prompt
while True:
    message = input(prompt)
    if message == 'quit':
        break
    age = int(message)
    if age < 3:
        print("The cost is free.")
    elif age < 12:
        print("The cost is 10$.")
    else:
        print("The cost is 15$.")
