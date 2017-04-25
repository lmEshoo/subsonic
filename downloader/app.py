from flask import Flask
from flask import request
import urllib, urllib2, json
from bs4 import BeautifulSoup
import subprocess

app = Flask(__name__)

@app.route("/", methods=['POST'])
def downloader():
#    try:
    for vid in BeautifulSoup(urllib2.urlopen\
        ("https://www.youtube.com/results?search_query=" + \
        urllib.quote(json.dumps(request.json['url'])) + \
        "audio").read()).findAll(attrs={'class':'yt-uix-tile-link'}):
        url= 'https://www.youtube.com' + vid['href']
        break
    subprocess.call("youtube-dl -x --embed-thumbnail --audio-format mp3 -o '/src/tmp/%(title)s.%(ext)s' " +url, shell=True)
    subprocess.call("sh upload.sh", shell=True)
    return "Got "+vid['title']+'.mp3'
#    except:
#        print "Couldn't get a song."

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port='5010')
