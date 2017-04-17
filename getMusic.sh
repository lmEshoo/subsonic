#!/bin/bash
#s3 bucket contains all my music called drake-more-life

aws s3 sync s3://drake-more-life /var/music
