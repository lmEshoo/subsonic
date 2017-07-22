#!/bin/bash
#s3 bucket contains all my music called drake-more-life

aws s3 sync s3://drake-more-life /var/s3

s3_directory_path=/var/s3/
music_directory_path=/var/music #organized music

find $s3_directory_path -name "*.mp3" -print0 | while read -d $'\0' file
do
  file_name="${file/$s3_directory_path/}"
  file_count=$(find $music_directory_path -name "$file_name" | wc -l)
  echo $file_name
  if [[ $file_count -gt 0 ]]; then
    echo "Warning: $file_name found $file_count times in $music_directory_path!"
  else
    echo "Error: $file_name not found in $music_directory_path!"
    cp $file $music_directory_path
  fi
done
