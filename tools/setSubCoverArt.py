#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script sets the song's cover arts and refreshes the library
"""
import os, difflib, urllib
import requests, os

files = [f for f in os.listdir('.') if os.path.isfile(f)]

songs = [k for k in files if '.mp3' in k]
images = [k for k in files if '.jpg' in k]
#print songs
#print images
#get rid of .mp3
songs_names=[]
for i in songs:
    songs_names.append(i.replace(".mp3",""))

for song in range(0,len(songs)):
    #match cover art with song
    image=difflib.get_close_matches(songs[song], images, 1, 0)[0]

    #set cover art path
    url = "http://"+os.environ.get('SUB_USER') \
        +":"+os.environ.get('SUB_PASS')+"@" \
        + os.environ.get('INSTANCE_IP') \
        +":4040/db.view?query=UPDATE%20media_file%20SET%20COVER_ART_PATH=%27/var/music/" \
        + urllib.quote( image.encode('utf-8')) \
        +"%27%20WHERE%20TITLE=%27" \
        + urllib.quote(difflib.get_close_matches( \
        songs[song], songs_names, 1, 0)[0].encode('utf-8')) +"%27;"
    payload = {'j_username': os.environ.get('SUB_USER'), 'j_password': os.environ.get('SUB_PASS')}
    r=requests.post(url, data=payload)
    #print r.text

#refresh library
url = "http://"+os.environ.get('SUB_USER') \
    +":"+os.environ.get('SUB_PASS')+"@" \
    + os.environ.get('INSTANCE_IP') \
    +":4040/rest/startScan?u=" \
    + os.environ.get('SUB_USER')+ "&p=" \
    +os.environ.get('SUB_PASS')+ "&v=1.15.0&c=app"
requests.post(url, data=payload)
