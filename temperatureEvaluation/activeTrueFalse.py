import sys
import os
import os.path

if os.path.isfile('/var/www/temperature-monitoring/temperatureEvaluation/aktuell.csv'):
    print 'Temperaturauslesen: aktiv'
    os.system("/var/www/temperature-monitoring/temperatureEvaluation/readTemperature.py")
else:
    print 'Temperaturauslesen: nicht aktiv'
    sys.exit(0)