motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print('-' * 10)



motorcycles.append('ducati')
#使用.append添加内容到末尾
print(motorcycles)
print('-' * 10)



motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
print('-' * 10)



motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#使用.insert将内容插入到指定位置
motorcycles.insert(0, 'ducati')
print(motorcycles)
print('-' * 10)



motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
print('-' * 10)



motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles_2 = []
print(motorcycles)
motorcycles_2.append(motorcycles.pop())
print(motorcycles_2)
#.pop默认将末尾的对象从列表中弹出,并且储存到新的变量中去
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print('-' * 10)



motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + \
      last_owned.title() + ".")
print('-' * 10)



motorcycles = ['honda', 'yamaha', 'suzuki']
#.pop()括号中可以填入想要弹出值的位置
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + \
      first_owned.title() + '.')
print('-' * 10)



motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
#.remove()可以删除列表中的指定值,并且可以接着使用
motorcycles.remove('ducati')
print(motorcycles)
print('-' * 10)



motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
#.remove删掉的值也可以继续使用
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too \
expensive for me.")
