def make_album(artist, album, tracks=''):
    result = {'artist': artist, 'album': album}
    if tracks:
        result['tracks'] = tracks
    return result


basta = make_album('basta', 'basta-5')
nirvana = make_album('kurt kobain', 'nirvana')
hoi = make_album('yourii hoi', '30 let')
manson = make_album('marilyn manson', 'fuck', '18')


print(basta)
print(nirvana)
print(hoi)
print(manson)
