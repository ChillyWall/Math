favorite_places = {
    'guo panpan': ['beijing', 'shanghai', 'tiananmen square'],
    'guo jinfeng': ['the great wall', 'zhengzhou', 'jinan'],
    'li ruixiang': ['hangzhou', 'nanjing', 'wuhan']
}

for name, places in favorite_places.items():
    print("\nName: " + name.title())
    print("Favorite places:")
    for place in places:
        print("\t\t\t" + place.title())
