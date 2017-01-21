# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 13:32:00 2017

@author: mikha
"""

import parseJSON

url = 'https://gist.githubusercontent.com/c2huc2hu/4164f3893e2c46c978a3159d307905ba/raw/a1eec746ee4c4c0bc1d3dc66fc4c6c07c3b81b7a/charging_stations.json'

def parseInput(inputString):
    parsed = inputString.split();
    return parsed;

def findDistance(inputString):
    lats,lngs,latd,lngd = parseInput(inputString)    
    
    #define key and base url
    api_key = 'AIzaSyAw6MXv804JDMInwU9YD1jZgVyOTaq4So8'
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    parameter = 'origins='+str(lats)+','+str(lngs)+\
    '&destinations='+str(latd)+','+str(lngd)+'&key='
    
    url = base_url + parameter + api_key 
    
    data = parseJSON(url)
    
    return (data)
    
def addToCache(parsedData):
    return