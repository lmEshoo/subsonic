from flask import Flask
from flask import request
import urllib, urllib2, json
from bs4 import BeautifulSoup
import subprocess, sys, coverart, time

app = Flask(__name__)

@app.route("/", methods=['POST'])
def downloader():
    try:
        #Get only videos
        for vid in BeautifulSoup(urllib2.urlopen\
            ("https://www.youtube.com/results?sp=EgIQAQ%253D%253D&q=" + \
            urllib.quote(json.dumps(request.json['url'])) + \
            "audio").read()).findAll(attrs={'class':'yt-uix-tile-link'}):
            url= 'https://www.youtube.com' + vid['href']
            break
    except:
        return "Wasn't able to reach youtube."
    try:
        #Download top result
        subprocess.call(\
            "youtube-dl -x --audio-format mp3 -o '/src/tmp/%(title)s.%(ext)s' " \
            +url, shell=True)
        time.sleep(1)
        subprocess.call("bash upload.sh", shell=True)
        return "Got "+vid['title']+'.mp3'
    except:
        return "Youtube Downloader failed."

@app.route("/better", methods=['POST'])
def better():
    try:    #donwload and upload
        subprocess.call("python instantmusic.py -p -q -s "\
            +request.json['name'], shell=True)
        time.sleep(1)
        subprocess.call("bash upload.sh", shell=True)
        return "Yooo I got it."
    except:
        return "Downloader failed to get a better song."

@app.route("/coverart", methods=['POST'])
def art():
    #try: #donwload and upload
    print request.json
    print request.json['name'] , request.json['image']
    subprocess.call("python instantmusic.py -p -s "\
        +request.json['name'].lower()+" song audio", shell=True)
    time.sleep(0.5)
    print "FINISHED DOWNLOADING"
    #Get getting the coverart
    coverart.getImage( \
        request.json['name'], \
        request.json['image'], \
        request.json['artist'] )
    time.sleep(0.5)
    subprocess.call("bash upload.sh", shell=True)
    return "Yooo I got it."
    # except:
    #     subprocess.call("bash upload.sh", shell=True)
    #     print "Error: getting coverart art failed"
    #     return "Yooo Something went wrong."

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port='5010')
