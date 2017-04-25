#!/bin/bash

if [ $1 = "up" ]; then
  cd downloader && make run
else
  cd downloader && make clean
fi
