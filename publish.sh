#!/bin/bash
git pull origin master
git add .
git commit -m "Update content"
git push origin master && lektor build && lektor deploy

