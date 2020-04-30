players = ['charles', 'martina', 'michael', 'florence', 'eli']
#输出范围内的列表元素
print(players[0:3])

#没有第一个索引时默认从0开始
print(players[ :4])

#没有第二个索引时默认为一直到最后一个
print(players[1:])
print("-" * 30)


print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
