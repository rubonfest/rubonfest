git add .

git commit -m "Update content"

git push origin master && lektor build -O build && rsync -avz build/ repo@bs.miesta.by:/var/www/rubon
