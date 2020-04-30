num_row = int(input("Please type the number of rows: "))
list_1 = []
for num in range(num_row):
    row = [1]
    list_1.append(row)

    if num == 0:
        print(row)
        continue

    for m in range(1, num):
        row.append(list_1[num - 1][m - 1] + list_1[num - 1][m])

    row.append(1)

    print(row)
