#!/usr/bin/env bash

curl -d '{
    "amount":"1.34"
}'     -H "Content-Type: application/json" -X POST https://us-central1-cloudai-194723.cloudfunctions.net/change722
