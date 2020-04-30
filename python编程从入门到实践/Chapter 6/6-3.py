vocabularies = {
    'integer': 'any number that is not a fraction or decimal : any whole number or its negative ',
    'float':"any number that has a '.'",
    'variable': "one or more strings ,which can only be with '_' and numbers and can't start with a number,\n\
are used to instead of any other things such as strings and numbers",
    'function': "函数, 用来存储一系列的代码, 对输入的参数进行运算",
    'module': "模块, 一个.py文件即为一个模板, 包括其中定义的所有函数, 还有代码.",
    'defined': "定义, 给一个变量赋值, 或者是给一个函数指定包括的代码.",
    'dictionary': "其中包括大量键-值对应的数据, 每一个数据都有键(key)和值(value)",
    'list': "列表, 其中包括了大量的值, 这些值都可以删除增加或者更改",
    '元组': "性质与列表相同, 但是其中的数据不能更改.",
    'block': "具有相同缩进量的的一组代码, 在同一个等级之内, 互相没有隶属关系."
}
for vocabulary in vocabularies:
    print("The meaning of {0} is {1}."
          .format(vocabulary, vocabularies[vocabulary]))
