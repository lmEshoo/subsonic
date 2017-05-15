import spotipy, subprocess, time, os
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from random import randint

client_credentials_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
songs=[]

#github.com/plamere/spotipy/blob/master/examples/artist_recommendations.py
def show_recommendations_for_artists(id):
    tmp=[]
    #sort, aggregate
    #get top 6 Recommendations
    results = spotify.recommendations(seed_artists = id, limit=10)
    print '\nRecommendations:'
    for track in results['tracks']:
        print str(track['name']).encode('utf-8') \
            + ' '+ str(track['artists'][0]['name']).encode('utf-8')
        tmp.append(tuple((\
            str(track['name']+ ' '+ track['artists'][0]['name']), \
            track['album']['images'][0]['url'] , track[u'artists'][0][u'name'] )))
    #pick a random song from top 3
    songs.append(tmp[randint(0,9)][:])

def fixLib(query):
    artist=spotify.search(q=query,type='artist')
    print query
    tmp=[]
    song=spotify.search(q=query,type='track')
    song_name = str(song[u'tracks'][u'items'][0][u'album'][u'name'])
    song_artist=song[u'tracks'][u'items'][0][u'artists'][0][u'name']
    song_art_url=song[u'tracks'][u'items'][0][u'album']['images'][0]['url']
    songs.append( tuple((str(query), song_art_url, song_artist)) )
    return tuple((str(query), song_art_url, song_artist))

#download
def sa():
    print 'Going to Download: \n', songs
    if len(songs) == 1:
        getSong(songs)
        songs.pop(0)
    else:
        for song in range(len(songs)):
            print "Song to Download:", songs[song]
            getSong(songs[song])

def getSong(song):
    print song
    subprocess.call(\
        "curl -X POST -H \
        'Content-Type: application/json' \
        -d '{ \"name\": \""+str(song[0])+"\", \"image\": \""+str(song[1])+"\", \"artist\": \""+str(song[2])+"\" }'  \
        http://"+os.environ.get('INSTANCE_IP')+":5010/coverart", shell=True)
    time.sleep(1)
    print ("Downloading", song)
    time.sleep(5)

#github.com/ayushr2/Music-Search-Engine/blob/master/app/spotify.py#L12
def get_id(query):
    print "GET ID (query): ", query
    artist=spotify.search(q=query,type='artist')
    song=spotify.search(q=query,type='track')
    song_name = str(song[u'tracks'][u'items'][0][u'album'][u'name'])
    song_artist=song[u'tracks'][u'items'][0][u'artists'][0][u'name']
    song_artist_id=song[u'tracks'][u'items'][0][u'artists'][0][u'id']

    return str(song_artist_id)

def recommend(query):
	ID_list=[]
	ID_list.extend([get_id(query)])
	show_recommendations_for_artists(ID_list)

	return "str1"
