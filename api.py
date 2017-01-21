# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 13:32:00 2017

@author: mikha
"""

import parseJSON

def parseInput(inputString):
    parsed = inputString.split()
    parsed = list(map(float,parsed))
    return parsed;

def findDistance(inputString):
    coords = parseInput(inputString)    
    
    #define key and base url
    api_key = 'AIzaSyAw6MXv804JDMInwU9YD1jZgVyOTaq4So8'
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    parameter = 'origins='+str(coords[0])+','+str(coords[1])+\
    '&destinations='+str(coords[2])+','+str(coords[3])+'&key='
    
    url = base_url + parameter + api_key 
    
    data = parseJSON(url)
    
    return (data)
    
def addToCache(parsedData):
    return