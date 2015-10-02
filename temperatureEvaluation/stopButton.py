#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import sys
import os
from time import *
import json
reload(sys)  
sys.setdefaultencoding('utf8')

lt = localtime()
Datum = strftime("%Y-%m-%d")
Uhrzeit = strftime("%H:%M:%S")

if os.path.isfile('/var/www/temperature-monitoring/temperatureEvaluation/aktuell.csv'):
    
    print "1"
    with open('/var/www/temperature-monitoring/temperatureEvaluation/projectname.json') as data_file:    
        data = json.load(data_file)
        print "2"
    
    print "3"
    os.rename("/var/www/temperature-monitoring/temperatureEvaluation/aktuell.csv", "/var/www/temperature-monitoring/temperatureEvaluation/readings/" + Datum + " " + Uhrzeit + " " + data["name"] + ".csv")
    os.system("/var/www/temperature-monitoring/temperatureEvaluation/checkHardwareButton.py")

sys.exit(0)