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
            track['album']['images'][0]['url']\
                )))
    #pick a random song from top 3
    songs.append(tmp[randint(0,9)][:])

#download
def sa():
    print 'Going to Download: \n', songs
    for i in range(len(songs)):
        subprocess.call(\
            "curl -X POST -H \
            'Content-Type: application/json' \
            -d '{ \"name\": \""+str(songs[i][0])+"\", \"image\": \""+str(songs[i][1])+"\" }'  \
            http://"+os.environ.get('INSTANCE_IP')+":5010/coverart", shell=True)
        time.sleep(1)
        print ("Downloading", songs[i])
        time.sleep(20)

#github.com/ayushr2/Music-Search-Engine/blob/master/app/spotify.py#L12
def get_id(query):
	artist=spotify.search(q=query,type='artist')
	#print query
	song=spotify.search(q=query,type='track')
	song_name = str(song[u'tracks'][u'items'][0][u'album'][u'name'])
	song_artist=song[u'tracks'][u'items'][0][u'artists'][0][u'name']
    song_art_url=song[u'tracks']['album']['images'][0]['url']
    
	song_genres= spotify.search(q=song_artist,type='artist') [u'artists'][u'items'][0][u'genres']
	#print song_genres[0:3]
	song_artist_id = song[u'tracks'][u'items'][0][u'artists'][0][u'id']
	print song_artist + ' - ' + song_name + ' (' + song_artist_id + ')'

	return str(song_artist_id)

def recommend(query):
	ID_list=[]
	ID_list.extend([get_id(query)])
	show_recommendations_for_artists(ID_list)

	return "str1"
