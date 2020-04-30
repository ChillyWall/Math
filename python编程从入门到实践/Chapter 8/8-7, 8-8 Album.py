def make_album(album_name, singer_names, song_number=''):
    album = {
        'the album name': album_name,
        'the singer\'s names': singer_names,
    }
    if song_number:
        album['the number of songs'] = song_number
    return album


while True:
    name = input("Please enter the name of the album: ")
    print("(Enter 'quit' to quit)")
    if name == 'quit':
        break

    singer = input("Please enter the name of name(s) of the singer(s): ")
    print("(Enter 'quit' to quit)")
    if singer == 'quit':
        break

    number_of_songs = input("Please enter the number of the songs: ")
    print("(Enter 'quit' to quit)")
    if number_of_songs == 'quit':
        break

    print(make_album(name, singer, number_of_songs))
