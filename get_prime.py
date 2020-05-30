def get_prime(start, end):
    """
    寻找范围内的质数，包括前一个和后一个
    原理：不是2、3、5、7的倍数的数都是质数
    :param start: 起始
    :param end: 结束
    :return: 一个包含范围内所有质数和非质数以及各自的数字及数量的字典
    """
    numbers = list(range(start, end + 1))
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
        'not prime': {
            'number': len(not_prime),
            'numbers': not_prime
        }
    }
    return final
