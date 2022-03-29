def make_album(artist, title, song=None):
    album = {
        'title': title,
        'artist': artist,
    }
    if song:
        album['song'] = song

    return album

print(make_album('love', 'arijit singh', 10))
print(make_album('tragedy', 'darshan raval', 5))
print(make_album('alone', 'sachet tanadon', 1))