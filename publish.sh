#!/bin/bash
git add .
git commit -m "Update content"
git push origin master && lektor.cmd build && lektor.cmd deploy

