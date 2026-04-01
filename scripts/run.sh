#!/bin/bash

ARCHIVE_DIR="./data/archives"
LOG_FILE="archiver.log"

echo "preparation environment..."

if [ ! -d "$ARCHIVE_DIR" ]; then
    echo "folder $ARCHIVE_DIR not found. Creating..."
    mkdir -p "$ARCHIVE_DIR"
else
    echo "folder is exist"
fi

echo "starting Docker..."
docker-compose -f ../archiver/docker/docker-compose.yml up -d --build

echo "service is ready on port 8080"
echo "you can see logs in $LOG_FILE"
date >> $LOG_FILE
