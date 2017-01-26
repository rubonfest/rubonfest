git add .

git commit -m "Update content"

git push origin master && lektor -O build build && lektor -O build deploy