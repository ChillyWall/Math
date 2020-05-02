dimensions = (200, 50)
#用()圈起来的列表称作"元组", 是不可改变的
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
