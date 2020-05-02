favorite_numbers = {
    'guo jinfeng': [7, 3, 4],
    'li ruixiang': [8, 4, 3],
    'guo panpan': [5, 6, 0],
    'guo yonghua': [8, 9, 1],
    'zhang chunzhi': [3, 8, 2],
    'wang huijie': [6, 2, 5],
}
for person, numbers in favorite_numbers.items():
    print(person.title() + "'s favorite number is:")
    for number in numbers:
        print("\t", number)
