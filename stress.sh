#!/bin/bash

if [ -z "$1" ]; then
  echo "Please, provide cluster ip as parameter"
  echo "Example: $0 123.123.12.1"
  echo "- If you are in Linux, you get the cluster ip using the command 'minikube ip'"
  echo "- If you are in windows, use 'localhost'"
  exit 1
fi

IP=$1

while true; do
    curl -X POST -H "Content-Type: application/json" \
    -d '{
        "user": "ana",
        "password": "batata123"
    }' http://$IP:30000/login
    sleep 0.01
done

