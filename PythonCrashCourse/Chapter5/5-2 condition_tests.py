car = 'audi'
print(car == 'audi')
print(car != 'bike')
print('-' * 30)

name = 'Harry'
print(name.lower() == 'harry')
print('-' * 30)

a = 1
b = 2
c = 1
print(a == c)
print(a != b)
print(a > b)
print(b < c)
print(b >= c)
print(c <= a)
print('-' * 30)

print(a > b or c < b)
print(a == c and b > a)
print('-' * 30)

l = list(range(0, 10, 2))
print(b in l)
print(a not in l)
