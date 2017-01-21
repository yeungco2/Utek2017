# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 16:16:38 2017

@author: mikha
"""

import json
import urllib

#helper function to turn input string into floats
def parseInputString(inputString):
    parsed = inputString.split()
    parsed = list(map(float,parsed))
    return parsed;

#parseFuelStation returns a list of dictionaries with the following keys
#in each dictionary: latitude, longitude, city, id
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
    
#parseGoogleAPI takes a input string a pair of longitudes and latitudes
#and formats a list of dictionaries with the following keys
#in each dictionary: distance(kilometers), duration(hours)
def parseGoogleAPI(inputString):
    coords = parseInputString(inputString)    
    
    #define key and base url
    api_key = 'AIzaSyAw6MXv804JDMInwU9YD1jZgVyOTaq4So8'
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    parameter = 'origins='+str(coords[0])+','+str(coords[1])+\
    '&destinations='+str(coords[2])+','+str(coords[3])+'&key='
    
    url = base_url + parameter + api_key 
    
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    data = data['rows'][0]['elements'][0]
    
    parsedData = []
    parsedData.append({'distance': (float("{0:.3f}".\
                        format(data['distance']['value']/1000.0))),\
                        'duration': (float("{0:.2f}".\
                        format(data['duration']['value']/3600.0)))})
    
    return parsedData