#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import sys
import os
from time import *
import json
reload(sys)  
sys.setdefaultencoding('utf8')


fobj_out = open("/var/www/temperature-monitoring/temperatureEvaluation/aktuell.csv","a")

fobj_out.write("DatumUhrzeit")
    
with open('/var/www/temperature-monitoring/temperatureEvaluation/sensornames.json') as data_file:    
    data = json.load(data_file)

for line in data:
    fobj_out.write("," + line["name"])
    
fobj_out.write("\n")
fobj_out.close()

os.system("/var/www/temperature-monitoring/temperatureEvaluation/checkHardwareButton.py")

sys.exit(0)