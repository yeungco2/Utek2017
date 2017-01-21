# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 16:16:38 2017

@author: mikha
"""

import json
import urllib

def parseFuelStation():
    url = 'https://gist.githubusercontent.com/c2huc2hu/'+\
    '4164f3893e2c46c978a3159d307905ba/raw/'+\
    'a1eec746ee4c4c0bc1d3dc66fc4c6c07c3b81b7a/charging_stations.json'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    
    parsedData = []
    for entry in data['fuel_stations']:
        parsedData.append({'latitude':entry['latitude'],\
                          'longitude':entry['longitude'],\
                          'city':entry['city'],\
                          'id':entry['id']})
                          
    return parsedData
    
def parseGoogleAPI(url):
    return