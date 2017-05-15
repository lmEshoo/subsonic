# -*- coding: utf-8 -*-
import eyed3
import subprocess, sys, os
import glob, time

def getImage(name, link, artist):
    name="".join(name.split())+".jpg"
    print "NEW: Getting Cover Art", name
    command="wget "+link+ " -q -O /src/tmp/"+name
    print "COMMAND: " + command
    subprocess.call(command, shell=True)
    print "Image Directory: ",str(glob.glob("/src/tmp/*"))
    time.sleep(0.5)
    appendCover(name,artist)

def appendCover(name, artist):
    print "NEW: Appending Cover Art"
    print "Song Directory: ",str(glob.glob("/src/tmp/*mp3")[0])
    audiofile = eyed3.load(glob.glob("/src/tmp/*mp3")[0])
    print "Image Directory: ",str(os.getcwd()+"/tmp/"+name)
    audiofile.tag.artist = artist.decode('utf-8')
    imagedata = open(os.path.join(os.getcwd()+"/tmp/")+name.split(' ')[0],"rb").read()
    check = audiofile.tag.images.set(3,imagedata,"image/jpeg")
    if check == None:
        print "Setting front cover error！"
        sys.exit(0)
    audiofile.tag.save()
