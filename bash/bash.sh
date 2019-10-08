#!/bin/bash

# Get top10
curl https://api.floodipdb.info/ip/top10

# Get info for a specific IP
curl -H "Content-type: application/json" -H "Accept: application/json" -d '{ "ip":"45.227.253.214" }' -X POST https://api.floodipdb.info/ip/info