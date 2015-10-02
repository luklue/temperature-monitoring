#!/bin/sh

val="$(gpio -g read 26)"
echo $val
if [ "$val" -eq "1" ]
then
    echo "An"
    sudo gpio -g write 26 0 
    python /var/www/temperature-monitoring/temperatureEvaluation/stopButton.py
else
    echo "Aus"
    sudo gpio -g write 26 1
    python /var/www/temperature-monitoring/temperatureEvaluation/startButton.py
fi