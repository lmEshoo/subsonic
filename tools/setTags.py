#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script sets the song's tags, creates paths for songs and refreshes the library
"""

import eyed3
import shutil
import os, difflib, urllib, time
import requests, os, json, re, glob, subprocess
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp_token = client_credentials_manager.get_access_token()

files = [f for f in os.listdir('.') if os.path.isfile(f)]

songs = [k for k in files if '.mp3' in k]
images = [k for k in files if '.jpg' in k]
songs_names=[]
for i in songs:
    songs_names.append(i.replace(".mp3",""))

print len(songs)
# print len(songs_names)

mkdir="mkdir -p /var/music/UNTITLED/UNTITLED_ALBUM/"
subprocess.call(mkdir, shell=True)

def infoSet(albums, index, last):
    audiofile = eyed3.load(str(songs[index]))

    if last is 1:

        #audiofile = eyed3.load(str(songs[os.listdir('.').index(songs[index])]).decode('utf-8'))
        image="".join(songs[index].split())
        image=difflib.get_close_matches(songs[song], images, 1, 0)[0]
        audiofile.tag.album = u"UNTITLED ALBUM"
        audiofile.tag.artist = u"UNTITLED ARTIST"
        audiofile.tag.album_artist = u"UNTITLED ARTIST"
        audiofile.tag.save()

        #move UNTITLED songs to right directory
        cp_image="mv /var/music/{0} /var/music/UNTITLED_ARTIST/UNTITLED_ALBUM/".format("'"+image+"'")
        cp_song="mv /var/music/{0} /var/music/UNTITLED_ARTIST/UNTITLED_ALBUM/".format("'"+songs[index]+"'")
        subprocess.call(cp_image, shell=True)
        subprocess.call(cp_song, shell=True)

    elif albums[u'tracks'][u'items'][0][u'album'][u'name']:

        #Get Track's album
        album=albums[u'tracks'][u'items'][0][u'album'][u'name']
        audiofile.tag.album = album.decode('utf-8')
        audiofile.tag.save()
        print "ALBUM: " + album

        if albums[u'tracks'][u'items'][0][u'album'][u'artists'][0][u'name']:

            #Get Track's artist
            artist=albums[u'tracks'][u'items'][0][u'album'][u'artists'][0][u'name']

            #create and move song and cover art to right Directory
            image=difflib.get_close_matches(songs[song], images, 1, 0)[0]
            print "IMAGE: "+image
            mkdir="mkdir -p /var/music/{0}/{1}/".format("'"+artist+"'","'"+album+"'")
            print "MKDIR: "+ mkdir
            subprocess.call(mkdir, shell=True)
            subprocess.call("mv /var/music/{0} /var/music/{1}/{2}/".format("'"+image+"'","'"+artist+"'","'"+album+"'"), shell=True)
            subprocess.call("mv /var/music/{0} /var/music/{1}/{2}/".format("'"+songs[index]+"'","'"+artist+"'","'"+album+"'"), shell=True)

            #if artist in songs[index]:
            audiofile.tag.artist = artist.decode('utf-8')
            audiofile.tag.album_artist = artist.decode('utf-8')
            print "ARTIST: " + artist
            audiofile.tag.save()

    else:
        print "Cannot find it."

#getAlbums takes sub argument that decides what the substrig cut off is
def getAlbums(sub):

    headers = {'Accept': 'application/json', 'Authorization': 'Bearer ' + sp_token}
    print "Retrying With: "+ re.sub("[\(\[].*?[\)\]]", "", " ".join(songs_names[song].replace("-","").replace(".","").replace(".mp3","").split()[:sub]))
    url = "https://api.spotify.com/v1/search?q="+urllib.quote(re.sub("[\(\[].*?[\)\]]", "", " ".join(songs_names[song].replace("-","").replace(".","").replace(".mp3","").replace(".mp3","").split()[:sub])).encode('utf-8') )+"&type=track&market=US"
    r=requests.get(url, headers=headers)
    albums= json.loads(r.text)
    # print albums
    return albums

def again(song):
    try:
        infoSet(getAlbums(3), song, 0)
    except:
        finalTry(song)
        #print "Renaming to UNTITLED.\n"

def finalTry(song):
    try:
        infoSet(getAlbums(2), song, 0)
    except:
        infoSet(getAlbums(2), song, 1)
        print "Renaming to UNTITLED.\n"

for song in range(0,len(songs)):
    #Try to get it's artist

    try:
        print song
        #cut-off, song, is it last?
        infoSet(getAlbums(4), song, 0)
    except:
        print song
        again(song)
        continue
    #time.sleep(0.5)

#refresh library
payload = {'j_username': os.environ.get('SUB_USER'), 'j_password': os.environ.get('SUB_PASS')}
url = "http://"+os.environ.get('SUB_USER') \
    +":"+os.environ.get('SUB_PASS')+"@" \
    + os.environ.get('INSTANCE_IP') \
    +":4040/rest/startScan?u=" \
    + os.environ.get('SUB_USER')+ "&p=" \
    +os.environ.get('SUB_PASS')+ "&v=1.15.0&c=app"
requests.post(url, data=payload)
