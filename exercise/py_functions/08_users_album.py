def make_album(artist, title):
    album = {
        'title': title,
        'artist': artist,
    }
    
    return album

while True:
    print("\nPlease enter the name of artist and album's title.")
    print("\nPlease press q or Q to quit.")
    album_title = input("Enter the name of the album: ")
    if album_title == 'q' or album_title == 'q'.upper():
        break
    album_artist = input("Enter the name of the artist: ")

    new_album = make_album(artist=album_artist, title=album_title)
    print(f"\n{new_album}")