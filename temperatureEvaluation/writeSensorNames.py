#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from time import *
import json
import commands
reload(sys)  
sys.setdefaultencoding('utf8')

file = open('/sys/devices/w1_bus_master1/w1_master_slaves')
w1_slaves = file.readlines()
file.close()

os.remove("/var/www/temperature-monitoring/temperatureEvaluation/sensornames.json")

fobj_out = open('/var/www/temperature-monitoring/temperatureEvaluation/sensornames.json','a')
fobj_out.write('[\n')

count = 0

for line in w1_slaves:

    w1_slave = line.split('\n')[0]
    
    file = open('/sys/bus/w1/devices/' + str(w1_slave) + '/w1_slave')
    
    filecontent = file.read()
    
    file.close()
    
    stringvalue = filecontent.split('\n')[1].split(' ')[9]
    
    temperature = float(stringvalue[2:]) / 1000

    count = count + 1
    str(count)
    
    fobj_out.write('{"id":"' + str(w1_slave) + '","name":"Name ' + str(count) + '"},\n')

fobj_out.close()

with open('/var/www/temperature-monitoring/temperatureEvaluation/sensornames.json','rb+') as filehandle:
    filehandle.seek(-2, os.SEEK_END)
    filehandle.truncate()

fobj_out = open('/var/www/temperature-monitoring/temperatureEvaluation/sensornames.json','a') 
fobj_out.write('\n]')
fobj_out.close()
 
commands.getstatusoutput('chmod o+rwx /var/www/temperature-monitoring/temperatureEvaluation/sensornames.json')



sys.exit(0)