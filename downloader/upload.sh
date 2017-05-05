#!/bin/bash
#s3 bucket contains all my music called drake-more-life

cd /src/tmp/ && fixalbumart
aws s3 sync /src/tmp s3://drake-more-life
rm /src/tmp/*
