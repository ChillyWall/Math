rivers = {
    '尼罗河': '埃及',
    '长江': '中国',
    '亚马孙河': '巴西',
}

for river, place in rivers.items():
    print(river.title() + "流经" + place.title())
