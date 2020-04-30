def total(a=5, *numbers, **phonebook):   #一个 * 表示所有的值都会被赋予numbers。
    print('a', a)
    #将numbers的所有值依次代入到single_item中，并完成下面的程序
    for single_item in numbers:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(10,1,2,3,Jack=1123, John=2231, Inge=1560))
