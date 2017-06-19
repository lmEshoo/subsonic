#!/bin/bash
#s3 bucket contains all my music called drake-more-life
rm -r /var/music/*
aws s3 sync s3://drake-more-life /var/s3
cp /var/s3/* /var/music/
