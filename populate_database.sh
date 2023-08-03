#!/bin/bash

pod_name=$(kubectl get pods --no-headers -o custom-columns=":metadata.name" | grep "hospital-api-deployment" | awk '{print $1; exit}')

if [ -z "$pod_name" ]; then
  echo "No pod containing 'hospital-api-deployment' found."
  exit 1
fi

echo "Executing populate script in pod: $pod_name"

kubectl exec -it $pod_name -- python src/api/populate_db.py

echo "Execution complete."
