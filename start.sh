#!/bin/bash
python3 /home/autoTest/LYZTest/CreateTestDateGk.py
cd /home/autoTest/LYZTest/report/HtmlReport
rm -f /home/docker/volumes/nginx-vol/_data/index.html
find  *.html |sort -r|head -n 1|xargs -i cp -f {} /home/docker/volumes/nginx-vol/_data/index.html