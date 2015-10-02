#!/bin/sh

cd /sys/class/gpio
echo "13" > export
echo "19" > export
echo "26" > export
echo "out" > gpio26/direction
echo "in" > gpio13/direction
echo "in" > gpio19/direction
cd

if [ -e "/var/www/temperature-monitoring/temperatureEvaluation/aktuell.csv" ]
then
    sudo gpio -g write 26 1
fi