import eyed3
import subprocess, sys, os
import glob, time

def getImage(name, link):
    print "Getting Cover Art"
    subprocess.call("wget "+link+ " -q -O /src/tmp/"+name+".jpg", shell=True)
    time.sleep(0.5)
    appendCover(name)

def appendCover(name):
    print "Appending Cover Art"
    audiofile = eyed3.load(glob.glob("/src/tmp/*mp3")[0])
    imagedata = open(os.path.join(os.getcwd()+"/tmp/")+name.split(' ')[0],"rb").read()
    audiofile.tag.images.set(3,imagedata,"image/jpeg",name)
    audiofile.tag.save()
