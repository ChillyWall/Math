print("让我们玩一个猜数字游戏")
x = int(input("你知道我现在想的是哪个数字吗？在这里输入:"))
t = 0
while t < 2:
    if x == 7:
        print("太神奇了，你竟然猜对了！")
        t = 4
    else :
        if x < 7 :
            print("小了！小了！")
        else :
            print("小了！小了！大了！大了！")
        x = int(input("再来一次:"))
    t = t + 1
if t == 3:
    print("猜了这么多次都不对，我们也太没默契了。")
else :
    if t == 0   :
        print("游戏结束，你对我真是太了解了。")1
        print("你是我肚子里的蛔虫吗？")
    else :
        print("虽然你猜错了一次，但对我还挺了解啊。")
