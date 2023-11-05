#!/bin/bash

# Ensure the container is running
container_id=$(docker ps -q -f "name=mycontainer")

#if [ -z "$container_id" ]; then
 #   echo "The container is not running."
  #  exit 1
#fi

# Copy output files from the container to the local machine (Windows path)
# Use Windows-style paths within the container
docker cp $container_id:/home/doc-bd-a3/res_dpre.csv /mnt/c/Users/Aly/bd-a3/
docker cp $container_id:/home/doc-bd-a3/eda-in-1.txt /mnt/c/Users/Aly/bd-a3/
docker cp $container_id:/home/doc-bd-a3/eda-in-2.txt /mnt/c/Users/Aly/bd-a3/
docker cp $container_id:/home/doc-bd-a3/eda-in-3.txt /mnt/c/Users/Aly/bd-a3/
docker cp $container_id:/home/doc-bd-a3/vis.png /mnt/c/Users/Aly/bd-a3/
docker cp $container_id:/home/doc-bd-a3/k.txt /mnt/c/Users/Aly/bd-a3/

# Stop and remove the container
docker stop $container_id
docker rm $container_id

echo "Files copied to C:/Users/Aly/bd-a3/ and container closed."

