current_users = ['harry', 'ron', 'hermione', 'dumbledore', 'malfoy']
new_users = ['harry', 'ron', 'malfoy', 'juli', 'bryce']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("This name has been used before.\nPlease try again.")
    else:
        print("This name hasn't been used before.")
