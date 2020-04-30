number = input("Enter a number, and I'll tell you if it's even or odd. ")
number_int = int(number)

if number_int % 2 == 0:
    print("\nThe number " + number + " is even.")
else:
    print("\nThe number " + number + " is odd.")
