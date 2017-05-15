#!/bin/bash

if [ $1 = "up" ]; then
  cd downloader && make run
elif [ $1 = "rec" ]; then
  cd recommender && make run
elif [ $1 = "post" ]; then
  #post processing
  while [[ ! `curl -sf http://$INSTANCE_IP:4040/login.view?` ]]; do sleep 5; done
  cd /var/music/ && python setSubCoverArt.py
  cd /var/music/ && python setTags.py
  cd /var/music/ && find . -name "*.mp3" -size -2000k -delete
  cd /app/tools/ && python refresh.py
else
  cd downloader && make clean
  cd ../recommender && make clean
  kill -9 `ps -aux | grep python | grep -v grep | awk '{ print $2 }'`
fi
