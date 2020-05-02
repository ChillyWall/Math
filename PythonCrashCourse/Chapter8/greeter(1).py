def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


# This is an infinite loop!
active = True
while active:
    print("\nPlease tell me your name: ")
    print("(enter 'quit' at any time to quit)")
    f_name = input("first name: ")
    if f_name == 'quit':
        print("Finished")
        break

    l_name = input("Last name: ")
    if l_name == 'quit':
        print("Finished")
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
