def make_album(artist, album, tracks=''):
    result = {'artist': artist, 'album': album}
    if tracks:
        result['tracks'] = tracks
    return result


while True:
    print('For quit enter "q"')
    print('Enter name of artist:')
    name = input()
    if name == 'q':
        break
    print('Enter album of artist:')
    album = input()
    if album == 'q':
        break
    print('Enter numbers of tracks in album, or press "enter" ')
    tracks = input()
    if tracks == 'q':
        break
    a = make_album(name, album, tracks)
    print(a)
