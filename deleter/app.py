#removes starred songs and refreshes the server.
from bs4 import BeautifulSoup
import requests, boto3, os, subprocess
from urllib2 import urlopen

r=requests.get("http://"+os.environ.get('SUB_USER') \
    +":"+os.environ.get('SUB_PASS')+"@" \
    + os.environ.get('INSTANCE_IP') \
    +":4040/db.view?query=SELECT%20media_file.PATH%20FROM%20media_file%20INNER%20JOIN%20STARRED_MEDIA_FILE%20ON%20STARRED_MEDIA_FILE.%20MEDIA_FILE_ID%20=media_file.ID;")
soup=BeautifulSoup(r.content)

s3client = boto3.client(
    's3',
    aws_access_key_id=os.environ.get('AWS_SUB_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SUB_SECRET_ACCESS_KEY')
    )

finished = False
tbl = soup.findAll('table')[0]
#print tbl
for tr in tbl.findAll('tr'):
    #print tr
    for td in tr.findAll('td'):
        if td.string.replace('/var/music/','') == "PATH":
            pass
        else:
            if td.string.count('/') > 3:
                #Print filename with path
                print td.string
                #Print filename only
                print os.path.basename(td.string)
                #Delete from s3
                response = s3client.delete_object(
                    Bucket='drake-more-life',
                    Key=os.path.basename(td.string)
                )
                #Remove locally from /var/music/<Song Name>
                subprocess.call("rm -rf {0} ".format("'"+td.string+"'"), shell=True)
                #Remove locally from /var/s3/<Song Name>
                subprocess.call("rm -rf /var/s3/{0} ".format("'"+os.path.basename(td.string)+"'"), shell=True)


#refresh subsonic library
payload = {'j_username': os.environ.get('SUB_USER'), 'j_password': os.environ.get('SUB_PASS')}
url = "http://"+os.environ.get('SUB_USER') \
    +":"+os.environ.get('SUB_PASS')+"@" \
    + os.environ.get('INSTANCE_IP') \
    +":4040/rest/startScan?u=" \
    + os.environ.get('SUB_USER')+ "&p=" \
    +os.environ.get('SUB_PASS')+ "&v=1.15.0&c=app"
requests.post(url, data=payload)


print 'Restarted.'
