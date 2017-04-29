#!/bin/bash

if [ $1 = "up" ]; then
  cd downloader && make run
elif [ $1 = "rec" ]; then
  cd recommender && make run
else
  cd downloader && make clean
  cd ../recommender && make clean
fi
