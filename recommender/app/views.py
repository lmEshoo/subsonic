from flask import Flask, request
from app import app
import spotify
import boto, os, hnhh
import time, subprocess

#get top songs of arists
@app.route('/recommend/artist',methods=['POST'])
def recommendArtist():
    #refresh my library (one time)
    artist_ids=[]
    refresh=[]
    artist = request.json['artist']
    print artist
    songs=spotify.recommend_tracks(artist)
    if songs:
        for song in songs:
            try:
                refresh.append(spotify.fixLib(song))
                spotify.sa()
                if songs.index(song) > 0:
                    spotify.songs.pop(0)
            except:
                # if songs.index(song) > 0:
                #spotify.songs.pop(0)
                continue
                # for i in range(3, 1, -1):
                #     #spotify.songs.pop(0)
                #     refresh.append(spotify.fixLib(' '.join(song.split()[:i])))
                #     spotify.sa()
            spotify.songs.pop(0)
        return "done"
    else:
        return "can't find artist"

#download specific songs
@app.route('/download',methods=['POST'])
def download():
    #refresh my library (one time)
    artist_ids=[]
    refresh=[]
    song = request.json['song']
    print song
    print spotify.songs
    try:
        refresh.append(spotify.fixLib(song))
        spotify.sa()
        spotify.songs.pop(0)
    except:
        for i in range(3, 1, -1):
            spotify.songs.pop(0)
            refresh.append(spotify.fixLib(' '.join(song.split()[:i])))
            spotify.sa()
            break

    return "done"


#recommend new songs
@app.route('/search',methods=['GET'])
def search():
    try:
        artist_ids=[]
        refresh=[]
        #get artist id
        for song in boto.get_s3():
            try:
                artist_ids.append(spotify.get_id(song))
                continue
            except:
                try:
                    artist_ids.append(spotify.get_id(' '.join(song.split()[:3]) ) )
                    continue
                except:
                    try:
                        artist_ids.append(spotify.get_id(' '.join(song.split()[:2]) ) )
                        continue
                    except:
                        continue
        #recommend only works for one to five seeds.
        artist_ids= [artist_ids[x:x+5] for x in range(0, len(artist_ids),5)]
        print artist_ids
        #get recommended songs (20 songs)
        for i in range(len(artist_ids)):
            #print artist_ids[i]
            try:
                spotify.show_recommendations_for_artists(artist_ids[i])
                time.sleep(1)
            except:
                pass
        spotify.sa()
        return "done"
    except:
        subprocess.call("cd .. && make restart", shell=True)
        return "spotify is down."

#Gets top 100 from HotNewHipHop
@app.route("/hnhh", methods=['GET'])
def specify_hnhh():
    songs=hnhh.hnhh_get_music()
    for song in songs:
        subprocess.call(\
            "curl -X POST -H \
            'Content-Type: application/json' \
            -d '{ \"name\": \""+str(song[0])+"\", \"image\": \""+str(song[1])+"\", \"artist\": \""+str(song[2])+"\" }'  \
            http://"+os.environ.get('INSTANCE_IP')+":5010/coverart", shell=True)
