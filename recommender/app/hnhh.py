from bs4 import BeautifulSoup
import urllib, urllib2, json, re

def hnhh_get_music():
    url = "http://www.hotnewhiphop.com/top100/"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)

    hnhh_songs_info = soup.find_all("div", class_="chartItem-body-artist")
    hnhh_songs_photo = soup.find_all("img", class_="chartItem-cover")
    hnhh_artist_info = soup.find_all("strong", class_="chartItem-artist-artistName")

    hnhh_songs=[]

    for i in range(0, 30):
        song_name=" ".join(re.findall("[a-zA-Z]+", hnhh_songs_info[i].a["title"] ))
        song_image=hnhh_songs_photo[i].get('src').replace("58x58","500x500")
        song_aritst=hnhh_artist_info[i].getText()
        hnhh_songs.append(tuple((song_name, song_image, song_aritst)))

    return hnhh_songs

# print hnhh_get_music()
