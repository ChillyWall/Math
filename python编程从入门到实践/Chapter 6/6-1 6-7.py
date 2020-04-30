info_guo_jinfeng = {
    'first': 'jinfeng',
    'last': 'guo',
    'age': 15,
    'birthday': 'April 22th',
    'city': 'pintyu',
}
info_li_ruixiang = {
    'first': 'ruixiang',
    'last': 'li',
    'age': 14,
    'birthday': 'October 10th',
    'city': 'pingyu'
}
info_guo_panpan = {
    'first': 'panpan',
    'last': 'guo',
    'age': 22,
    'birthday': 'unknown',
    'city': 'pingyu'
}

people = [info_guo_jinfeng, info_guo_panpan, info_li_ruixiang]

for info in people:
    full_name = info['last'] + ' ' + info['first']
    print("\nFull name: " + full_name.title())
    print("\tAge: " + str(info['age']))
    print("\tBirthday: " + info['birthday'])
    print("\tCity: " + info['city'].title())
