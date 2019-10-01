#!/usr/bin/env python3
import requests

r = requests.get('https://api.floodipdb.info/totalIp')
print(r.json())