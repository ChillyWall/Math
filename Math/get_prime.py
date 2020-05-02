def get_prime(a, b):

    """用来找到数字范围内的的质数
    原理:将范围内所有是2,3,5,7的倍数的数全部去掉,剩下的即是质数"""

    numbers = list(range(a, b + 1))
    prime = []
    not_prime = []

    for number in numbers:
        if number == 2:
            prime.append(number)
        elif number == 3:
            prime.append(number)
        elif number == 5:
            prime.append(number)
        elif number == 7:
            prime.append(number)
        elif number % 2 == 0:
            not_prime.append(number)
        elif number % 3 == 0:
            not_prime.append(number)
        elif number % 5 == 0:
            not_prime.append(number)
        elif number % 7 == 0:
            not_prime.append(number)
        else:
            prime.append(number)

    final = {
        'prime': {
            'number': len(prime),
            'numbers': prime
        },
        'not prime':{
            'number': len(not_prime),
            'numbers': not_prime
        }
    }
    return final
