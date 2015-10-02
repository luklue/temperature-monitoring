#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from time import *
import json
reload(sys)  
sys.setdefaultencoding('utf8')

lt = localtime()
Datum = strftime("%Y-%m-%d")
Uhrzeit = strftime("%H:%M")

file = open('/sys/devices/w1_bus_master1/w1_master_slaves')
w1_slaves = file.readlines()
file.close()

fobj_out = open("/var/www/temperature-monitoring/temperatureEvaluation/aktuell.csv","a")
fobj_out.write(Datum + " " + Uhrzeit)

for line in w1_slaves:

    w1_slave = line.split("\n")[0]
    
    file = open('/sys/bus/w1/devices/' + str(w1_slave) + '/w1_slave')
    
    filecontent = file.read()
    
    file.close()
    
    stringvalue = filecontent.split("\n")[1].split(" ")[9]
    
    temperature = float(stringvalue[2:]) / 1000
    
    with open('/var/www/temperature-monitoring/temperatureEvaluation/sensornames.json') as data_file:    
        data = json.load(data_file)
    
    fobj_out.write("," + '%5.3f' % temperature)
    
fobj_out.write("\n")
fobj_out.close()

sys.exit(0)