#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv/  
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio  
import sys
import os
import RPi.GPIO as GPIO
import os.path

GPIO.setmode(GPIO.BCM)  
  
# GPIO 13 set up as input. It is pulled up to stop false signals  
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

print "During this waiting time, your computer is not"   
print "wasting resources by polling for a button press.\n"  
print "Press your button when ready to initiate a falling edge interrupt."  
try:  
    GPIO.wait_for_edge(13, GPIO.FALLING)  
    print "\nFalling edge detected. Now your program can continue with"  
    print "whatever was waiting for a button press."
    os.system("/var/www/temperature-monitoring/temperatureEvaluation/checkLed.sh")
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit 