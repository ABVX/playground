#!/bin/bash
container="docker-archiver-1"

git pull
docker compose up -d --build

health=$(docker inspect --format='{{.State.Health.Status}}' $container)

if [ "$health" == "healthy" ]; then
  echo "Deploy successful"
else
  echo "Deploy failed"
  docker logs $container
fi
