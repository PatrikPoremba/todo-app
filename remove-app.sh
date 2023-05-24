#!/bin/bash

echo "Deleting Kubernetes resources..."
kubectl delete -f namespace.yaml -f deployment.yaml -f service.yaml
kubectl delete namespace todoapp

echo "App removed successfully."
