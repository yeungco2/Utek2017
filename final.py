# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 13:32:00 2017

@author: mikha
"""

import parseJSON

def partTwo(input):
    data = parseGoogleAPI(input)
    result = str(data[0]['distance'])+' '+str(data[0]['duration'])
    print(result)
    return