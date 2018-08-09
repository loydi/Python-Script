#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import requests
import simplejson as json

url = "http://example.com/reverse?format=json&zoom=17&addressdetails=1&lat=40.90182&lon=40.19762"
params = dict(
        place_id ='1415307'

     )

r = requests.get(url=url,params=params)
ra = r.json()
if ra['place_id'] =='1415307':
    print ('System is running.. : OK')
    exit (0)
else:
    print ('System is not running')
    exit (2)