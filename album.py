'''
Created on Dec 27, 2023

@author: apurs
'''

def make_album(artist, album, number = None):
    if number:
        album_dictionary = {'artist':artist.title(), 'album':album.title(), 'number':number}
    else:
        album_dictionary = {'artist':artist.title(), 'album':album.title()}
    return album_dictionary

# print(make_album('coldplay', 'yellow'))
# print(make_album('nickleback', 'silver side up'))
# print(make_album('creed', 'clay man', 25))

while True:
    print("\nPlease tell the artist and album:")
    print("(enter 'q' at any time to quit)")
    artist = input("artist:")
    if artist == 'q':
        break
    album = input("album:")
    if album == 'q':
        break
    album_build = make_album(artist, album)
    print(f"\n {album_build}")