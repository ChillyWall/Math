def print_max(x, y):    #定义一个函数
    '''Prints the maximum of weo numbers.

    The two values must be integers.'''

    #将x、y转换为整数
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
