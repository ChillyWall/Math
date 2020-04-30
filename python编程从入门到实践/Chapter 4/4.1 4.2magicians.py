magicians = ['alice', 'david', 'carolina']
#我们定义了一个for 循环, 从列表中取出一个名字，并将其存储在变量中。
#这样，对于列表中的每个名字，Python都将重复执行下面的代码行。

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wat to see your next trick, " + magician.title() + ".\n")

#没有缩进所以没有进入循环,只会在最后打印一次
print("Thank you, everyone. That was a great magic show!")
