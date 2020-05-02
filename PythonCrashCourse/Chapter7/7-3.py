number = input("If you tell me a number, I can tell you if it's a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print("Yes, it is a multiple of 10.")
elif number % 10 != 0:
    print("No, it is not a multiple of 10.")
