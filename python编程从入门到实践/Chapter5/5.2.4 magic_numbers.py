answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

#只有and两边均为True的时候整个结果才会显示为True
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)


#只要or的两边有一个时True,结果都未True
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)


requested_toppings = ['mushrooms', 'onions', 'pineapple']
#in用来判断特定值是否在列表中
print('mushrooms' in requested_toppings)
print('pepperon' in requested_toppings)


