class ListNumbers:
    """
    List the numbers with 1, 2**0.5, 3**0.5, 6**0.5 in order
    """
    def __init__(self, row_number):
        self.row_num = row_number
        self.the_list = self.make_list()
        self.print_list()

    def make_list(self):
        """
        make the list of numbers
        :return:
        """
        num1 = u"  1   "
        num2 = u"2**0.5"
        num3 = u"3**0.5"
        num4 = u"6**0.5"
        timer_row = 0
        w_num = 1
        numbers = []
        while timer_row < self.row_num:
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

    def print_list(self):
        """
        print the list
        :return:
        """
        for row in self.the_list:
            for number in row:
                print(number, end="")


def calculate(first_row, first_num, second_row, second_num):
    """
    multiply the first number and second number
    :param first_row: the row of the first numbers in
    :param first_num: the index of the first numbers
    :param second_row: the row of the second number
    :param second_num: the index of the second number
    :return: the product of the two numbers
    """
    row_num = max(first_row, second_row)
    numbers = ListNumbers.make_list(row_num)
    first = numbers[first_row - 1][first_num - 1]
    second = numbers[second_row - 1][second_num - 1]
    number = int(first[0]) * int(second[0])
    return str(number) + " ** 0.5"
