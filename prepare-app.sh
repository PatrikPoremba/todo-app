#!/bin/bash

echo "Building the Docker image..."
docker build -t todo-app .

echo "Running the Docker container..."
docker run -d -p 5000:5000 --name todo-app-container todo-app

echo "Waiting for the container to start..."
sleep 5

echo "Displaying the container logs..."
docker logs todo-app-container
