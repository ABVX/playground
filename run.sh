#!/bin/bash

if  [ -f "index.html" ]; then
	rm index.html
	echo "Old index.html file will be deleted"
fi

echo "Start archive..."
docker-compose up

if [ -f "index.html" ]; then
	echo "Ready. Check index.html"
	ls -lh index.html
else 
	echo "Error cannot find index.html"
fi
