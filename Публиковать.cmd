git add .

git commit -m "Update content"

git push origin master && lektor --output-path build build && lektor --output-path build deploy