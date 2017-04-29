from flask import Flask, request
from app import app
import spotify
import boto
import time

@app.route('/search',methods=['GET'])
def search():
    #try:
    artist_ids=[]
    #get artist id
    for song in boto.get_s3():
        try:
            artist_ids.append(spotify.get_id(song))
        except:
            try:
                artist_ids.append(spotify.get_id(' '.join(song.split()[:3]) ) )
            except:
                artist_ids.append(spotify.get_id(' '.join(song.split()[:2]) ) )
    #recommend only works for one to five seeds.
    artist_ids= [artist_ids[x:x+5] for x in range(0, len(artist_ids),5)]
    #get recommended songs (20 songs)
    for i in range(len(artist_ids)):
        #print artist_ids[i]
        spotify.show_recommendations_for_artists(artist_ids[i])
        time.sleep(1)
    
    spotify.sa()
    return "done"
#except:
#    return "spotify is down."
