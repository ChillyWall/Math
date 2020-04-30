def show_magicians(magicians):
    make_great(magicians)
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = 'the Great, ' + magicians[i]


magicians = ['liu qian', 'tom']
show_magicians(magicians[:])
print(magicians)
