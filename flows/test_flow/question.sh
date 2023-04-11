#!/bin/bash

question=$1

payload_json=$(echo '{}' | jq --arg p "$question" '. + {parameters:{question: $p}}')

echo $payload_json

curl -X 'POST' \
  'http://localhost:4200/api/deployments/1ad4da7c-0906-4a47-910f-e515f65a68b8/create_flow_run' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d "$payload_json"
