#!/usr/bin/env python3
import requests
import json

r = requests.get('https://api.floodipdb.info/totalIp')
print(r.json())

payload = {'ip': '45.227.253.214'}
r = requests.post('https://api.floodipdb.info/ip/info', json=payload)
print(r.json())
