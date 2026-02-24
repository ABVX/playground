#!/bin/bash

if  [ -f "index.html" ]; then
	rm -f index.html
	echo "Old index.html file will be deleted"
fi

echo "Start archive..."
docker-compose up -d

echo "waiting for archiver to finish..."
until [ -f index.html ]
do
	sleep 1
done
echo "File found! Starting web server"

if [ -f "index.html" ]; then
	echo "Ready. Check index.html"
	ls -lh index.html
else 
	echo "Error cannot find index.html"
fi
