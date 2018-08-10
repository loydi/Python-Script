#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import requests
import simplejson as json

url = "http://example.com/api/v1/address?lat=41.0&long=29.0"
headers = {'X-AuthToken':'54e1df6fe3ab09086c6578946b0e376b96b79a357b2bd2072b7d8872284b8bce0f018dbd'}
r = requests.get(url=url, headers=headers)
ra = r.json()

if ra['status'] =='OK':
    print ('System is running.. : OK ')
    exit (0)
else:
    print ('System is not running')
    exit (2)