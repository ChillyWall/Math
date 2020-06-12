class ListNumbers:
    the_list = []
    row_num = 0

    def __init__(self, row_number):
        ListNumbers.row_num = row_number
        ListNumbers.the_list = ListNumbers.make_list(row_number)
        ListNumbers.print_list()

    @classmethod
    def make_list(cls, row_num):
        num1 = u"1"
        num2 = u"2 ** 0.5"
        num3 = u"3 ** 0.5"
        num4 = u"6 ** 0.5"
        timer_row = 0
        w_num = 1
        numbers = []
        while timer_row < row_num:
            timer_num = 0
            numbers_used = []
            while timer_num < timer_row + 1:
                if w_num == 1:
                    numbers_used.append(num1)
                elif w_num == 2:
                    numbers_used.append(num2)
                elif w_num == 3:
                    numbers_used.append(num3)
                elif w_num == 4:
                    numbers_used.append(num4)
                    w_num = 0
                w_num += 1
                timer_num += 1
            numbers.append(numbers_used)
            timer_row += 1
        return numbers

    @staticmethod
    def print_list():
        for number in ListNumbers.the_list:
            print(number)

    @classmethod
    def calculate(cls, first_row, first_num, second_row, second_num):
        row_number = max(first_row, second_row)
        numbers = ListNumbers.make_list(row_number)
        first = numbers[first_row - 1][first_num - 1]
        second = numbers[second_row - 1][second_num - 1]
        number = int(first[0]) * int(second[0])
        return str(number) + " ** 0.5"


num = ListNumbers.calculate(5, 4, 15, 2)
print(num)