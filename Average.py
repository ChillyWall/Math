class Average:
    @classmethod
    def __init__(cls, numbers, weight=(), completed=False):
        cls.numbers = numbers
        cls.weight = weight
        cls.completed = completed
        cls.final = Average.get_all(numbers, weight, completed)
        if weight:
            cls.weighted_average = cls.final['weighted average']
            if completed:
                cls.completed_numbers = cls.final['completed numbers']
        else:
            cls.average = cls.final['average']
        cls.median = cls.final['median']
        cls.public = cls.final['public']
        cls.variance = cls.final['variance']

    @classmethod
    def get_weighted_average(cls, weight, numbers):
        """
        计算加权平均数
        :param weight: 权
        :param numbers: 数据
        :return: 加权平均数
        """
        value = 0
        for index in range(0, len(weight)):
            # 遍历列表, 将对应的数据和权相乘并相加并写进变量
            value += numbers[index] * weight[index]
        return value / sum(weight)

    @classmethod
    def get_group_value(cls, *limits):
        """
        计算小组的组中值
        :param limits: 小组的两边数，每一对在一个列表
        :return: 组中值（列表）
        """
        weight = []
        for limit in limits:
            weight.append(Average.get_average(limit))
        return weight

    @classmethod
    def get_average(cls, numbers):
        """
        计算算术平均数，格式为列表
        :param numbers: 数据
        :return: 平均数（浮点数）
        """
        return sum(numbers) / len(numbers)

    @classmethod
    def get_median(cls, numbers):
        """
        计算中位数
        :param numbers: 数据
        :return: 中位数（整数或浮点数）
        """
        numbers_used = numbers[:]
        numbers_used.sort()
        num = len(numbers)

        # 如果有偶数个数据， 输出中间两个数据的平均值
        # 如果有奇数个数据， 输出正中间的数据
        if num % 2 == 0:
            index = num // 2 - 1
            return Average.get_average([numbers_used[index], numbers_used[index + 1]])
        else:
            index = (num + 1) // 2 - 1
            return numbers_used[index]

    @classmethod
    def get_public(cls, numbers):
        """
        计算众数
        :param numbers: 数据
        :return: 众数（列表）
        """
        used_numbers = {}

        # 将实参遍历一遍
        # 将每一个不重复的数字存储在字典的键中, 次数为1
        # 数字美重复一次次数加一
        for i in range(len(numbers)):
            if numbers[i] in used_numbers.keys():
                used_numbers[numbers[i]] += 1
            else:
                used_numbers.setdefault(numbers[i], 1)

        public = []
        max_times = max(used_numbers.values())

        # 遍历字典, 找出出现次数最多的键值对的键并存储在最终列表中
        for key, value in used_numbers.items():
            if value == max_times:
                public.append(key)

        return public

    @classmethod
    def get_variance(cls, numbers):
        """
        计算数据的方差
        :param numbers: 数据
        :return: 方差（浮点数）
        """

        n = len(numbers)   # 数据的数量
        x_ = Average.get_average(numbers)    # 平均值
        numerator = 0

        # 遍历字典，
        for index in range(n):
            numerator += pow(numbers[index] - x_, 2)
        variance = numerator / n
        return variance

    @classmethod
    def complete(cls, numbers, weight):
        """
        当权是指数据出现次数时数据补全
        即使列表中存在对应次数的数据
        :param numbers: 数据
        :param weight: 权（出现次数）
        :return: 补全后的数据（列表）
        """
        completed_numbers = []
        for i in range(len(numbers)):
            times = 0
            while times < int(weight[i]):
                completed_numbers.append(numbers[i])
                times += 1
        return completed_numbers

    @classmethod
    def get_all(cls, numbers, weight=(), completed=False):
        """
        计算数据的平均数、中位数、众数、方差
        :param numbers: 数据
        :param weight: 数据的权，可以忽略
        :param completed: 是否按照权（数据出现次数）进行补全
        :return: 包含所有数据的字典，包括数据、权（如果有）、补全后的数据（如果确定要补全并且有权）、加权平均数（或算术平均数）、
                 众数、中位数、方差
        """
        all_numbers = {'numbers': numbers}
        if weight:
            weighted_average = Average.get_weighted_average(weight, numbers)
            all_numbers['weight'] = weight
            all_numbers['weighted average'] = weighted_average
            if completed:
                completed_numbers = Average.complete(numbers, weight)
                all_numbers['completed numbers'] = completed_numbers
                median = Average.get_median(completed_numbers)
                public = Average.get_public(completed_numbers)
                variance = Average.get_variance(completed_numbers)

            else:
                median = Average.get_median(numbers)
                public = Average.get_public(numbers)
                variance = Average.get_variance(numbers)

        else:
            median = Average.get_median(numbers)
            public = Average.get_public(numbers)
            variance = Average.get_variance(numbers)
            all_numbers['average'] = Average.get_average(numbers)
        
        all_numbers['median'] = median
        all_numbers['public'] = public
        all_numbers['variance'] = variance

        return all_numbers

    @classmethod
    def print_all(cls, all_numbers):
        """
        将使用get_all函数得出的数据打印出来
        :param all_numbers: get_all函数返回的字典
        :return: 无
        """
        for key, value in all_numbers.items():
            if type(value) != list:
                print("The {0} is {1}".format(key, value))
            else:
                if len(value) > 1:
                    print("The {0} are {1}".format(key, value))
                else:
                    print("The {0} is {1}".format(key, value))
