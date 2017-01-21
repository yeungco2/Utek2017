# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 13:32:00 2017

@author: mikha
"""

import json
import urllib

def findDistance(lats, lngs, latd, lngd):
    #define key and base url
    api_key = 'AIzaSyAw6MXv804JDMInwU9YD1jZgVyOTaq4So8'
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    parameter = 'origins='+str(lats)+','+str(lngs)+\
    '&destinations='+str(latd)+','+str(lngd)+'&key='
    
    url = base_url + parameter + api_key 
    
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    
    return (data)
    