import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser
import random

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
arjit_uri = 'https://open.spotify.com/artist/4YRxDV8wJFPHPTeXepOstw?si=fDqYt4_QSCyZtia6h18HqA'
happy_uri = "https://open.spotify.com/playlist/4nd7oGDNgfM0rv28CQw9WQ?si=6df8abb671c644fc"
sad_uri = "https://open.spotify.com/playlist/0z5GPu1ZL2ryEmPbTyH0tB?si=1b6070016aec4611"

# resuri = "http://localhost:8080/callback"

# safe_chars = ":/"
# encoded_url = quote(resuri, safe=safe_chars)

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="747949cf69ba42c28abe444d0788424f",client_secret="a182f4942f3042bd9cdd09954c6fc01f"))
# spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="747949cf69ba42c28abe444d0788424f",client_secret="a182f4942f3042bd9cdd09954c6fc01f",redirect_uri = encoded_url,scope = 'user-library-read'))

# To search album of artist
# results = spotify.artist_albums(birdy_uri, album_type='album')
# results = spotify.playlist(sad_uri)
# print(results.keys())
# for item in results['tracks']['items']:
#     uri = item['track']['uri']
#     print(item['track']['uri'])
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])


# albums
# artists
# episodes
# genres
# playlists
# podcasts
# tracks


# for album in albums:
#     print(album['name'])

# def test():
#     type = 'track'
#     name = input('Enter song name: ')
#     results = spotify.search(q=name, type=type)
#     # results = spotify.search(q=name, type='playlist')

#     res = results[type+'s']['items']

#     # print(results['playlists']['items'][0]['name'])

#     # Get the URI of the first result
#     # item = results['tracks']['items'][0]

#     # Play the song using the URI
#     # spotify.start_playback(uris=[uri])

#     songList = []
#     for item in res:
#         print(item['name'],item['uri'])
#         songList.append(item)

#     rand = random.randint(1,len(songList))

#     # webbrowser.open(results['tracks']['items'][0]['uri'])
#     song = songList[rand-1]['uri']
#     webbrowser.open(song)

def track(uri):
    results = spotify.playlist(uri)
    playlistName = results['name']
    print('\nPlaylist Name: '+ playlistName)
    res = results['tracks']['items']
    # print("Result:")
    # dict_keys(['album_type', 'artists', 'available_markets', 'external_urls', 'href', 'id', 'images', 'name', 'release_date', 'release_date_precision', 'total_tracks', 'type', 'uri'])
    
    songList = []
    for item in res:
        # print(item['track']['name'], item['track']['uri'])
        songList.append(item)
    rand = random.randint(1,len(songList))-1

    # webbrowser.open(results['tracks']['items'][0]['uri'])
    songUri = songList[rand]['track']['uri']
    songName = songList[rand]['track']['name']
    AlbumName = songList[rand]['track']['album']['name']
    max = 0
    imgUrl = ''
    for img in songList[rand]['track']['album']['images']:
        if img['height'] > max:
            max = img['height']
            imgUrl = img['url']

    webbrowser.open(songUri)
    print('SongName: ' + songName)
    dic = {'song': songName,'playlist':playlistName,'imgUrl':imgUrl,'AlbumName':AlbumName}
    return dic

# def playlist(name):
#     results = spotify.search(q=name, type='playlist')
#     # results = spotify.search(q=name, type='playlist')

#     res = results['playlists']['items']

#     songList = []
#     for item in res:
#         print(item['name'],item['uri'])
#         songList.append(item)

#     rand = random.randint(0,len(songList)-1)
#     rand = 0
#     playlistUri = songList[rand]['uri']
#     playlistName = songList[rand]['name']
#     # webbrowser.open(playlist)
#     track(playlistUri)
#     print('Playlist Name: ' + playlistName)

# # name = input('Enter song name: ')
# # playlist(name)

def selectPlaylist(emotion,lang):
    playlist = {
        'happyHindi':'https://open.spotify.com/playlist/4nd7oGDNgfM0rv28CQw9WQ?si=f051a8b0e0b84ab9',
        'sadHindi':'https://open.spotify.com/playlist/0z5GPu1ZL2ryEmPbTyH0tB?si=7fb986b96b714a5c',
        'fearHindi':'https://open.spotify.com/playlist/54i4ygGRUiT04Ro6ZcsXqo?si=5d1becd2d8444d49',
        'angryHindi':'https://open.spotify.com/playlist/0YMghmr5hSy2rrkL4BVuHP?si=8357b063ea474084',
        'neutralHindi':'https://open.spotify.com/playlist/27FQ0JN40Fg5IDXUdGRJUS?si=5252e9331c6c40c0',
        'disgustHindi':'https://open.spotify.com/playlist/1eXlmh5DI8nkxd2YZYGsy5?si=2b6ea68ae8f94160',
        'supriseHindi':'https://open.spotify.com/playlist/1qk7sHSUKBuKeDaMeTQqMY?si=3d63571d9f654c4c',

        'happyEnglish':'https://open.spotify.com/playlist/0jrlHA5UmxRxJjoykf7qRY?si=9c6abe216cf24bf3',
        'sadEnglish':'https://open.spotify.com/playlist/1FRwmEn9AXk00QXsJftM3m?si=a9a490a1836f4470',
        'fearEnglish':'https://open.spotify.com/playlist/0SKDsYUwb8jlqKADTJAiBY?si=65a141e39f9c422f',
        'angryEnglish':'https://open.spotify.com/playlist/67STztGl7srSMNn6hVYPFR?si=ad63636c6b714371',
        'neutralEnglish':'https://open.spotify.com/playlist/7msgpEqduZvJT2lqUMlM1J?si=0e92f6f357964114',
        'disgustEnglish':'https://open.spotify.com/playlist/7tkuMGECLRUPuSj5SY2ErP?si=47df8b6c15cf4e64',
        'supriseEnglish':'https://open.spotify.com/playlist/3Zu0J0JzSRzAT32LgFyg7i?si=201732563bf44707',

        'happyKannada':'https://open.spotify.com/playlist/37i9dQZF1DX1ahAlaaz0ZE?si=mAUOEaj3SeWrOzfuXeZGfg',
        'sadKannada':'https://open.spotify.com/album/3heIMtSen3osCkA3otiuCI?si=mnlr2PopS7a8F_c-Mi1pXg',
        'fearKannada':'https://open.spotify.com/playlist/1C2ZX32E6c5FgOwD3OWsbl?si=Lqg8JR1BR7Wo-aMZKYrp9Q',
        'angryKannada':'https://open.spotify.com/playlist/37i9dQZF1DX9i6vCEoH6jH?si=HivcDcL-Q1KrlQX3mRXANQ',
        'neutralKannada':'https://open.spotify.com/playlist/5JvdtbtyDhOWPApaRVY4wC?si=HQm9bH6rSrGwhJ8wklVcdw',
        'disgustKannada':'https://open.spotify.com/playlist/7tkuMGECLRUPuSj5SY2ErP?si=47df8b6c15cf4e64',
        'supriseKannada':'https://open.spotify.com/playlist/37i9dQZF1DX2MvScOHAAiE?si=ZvAOAOS3RWG5q8MN_7Yu7Q'
        }
    res = track(playlist[emotion+lang])
    return res
