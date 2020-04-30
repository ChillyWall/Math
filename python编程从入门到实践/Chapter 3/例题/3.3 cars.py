cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
#.sort()默认将列表按字母顺序排序
cars.sort()
print(cars)
print('_' * 30)



cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
#使用.sort(reverse=True)按照字母的反顺序进行排序
cars.sort(reverse=True)
print(cars)
print('_' * 30)



cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the orginal list")
print(cars)
#同.sort(reverse=True)进行排序,但是不会真的进行修改
print("\nHere is the sorted list")
print(sorted(cars, reverse=True))

print("\nHere is the original list again")
print(cars)
print('_' * 30)



cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
#.reverse()将列表顺序反过来
cars.reverse()
print(cars)
print('_' * 30)



cars = ['bmw', 'audi', 'toyota', 'subaru']
#len()可以确定列表的元素数量
print(len(cars))
