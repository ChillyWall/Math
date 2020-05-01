# users = ['harry', 'ron', 'hermione', 'dumbledore', 'malfoy', 'admin']
users = []
if users:
    for user in users:
        if not users:
            print("We need to find some users!")
        if user == 'admin':
            print("Hello {0}, would you like to see a status report?".format(user.title()))
        else:
            print("Hello {0}, thank you for logging in again.".format(user.title()))
else:
    print("We need to find users.")
