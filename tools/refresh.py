import os, time
import requests
#refresh subsonic library
payload = {'j_username': os.environ.get('SUB_USER'), 'j_password': os.environ.get('SUB_PASS')}
url = "http://"+os.environ.get('SUB_USER') \
    +":"+os.environ.get('SUB_PASS')+"@" \
    + os.environ.get('INSTANCE_IP') \
    +":4040/rest/startScan?u=" \
    + os.environ.get('SUB_USER')+ "&p=" \
    +os.environ.get('SUB_PASS')+ "&v=1.15.0&c=app"
requests.post(url, data=payload)
