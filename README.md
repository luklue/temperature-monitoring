# Temperature monitoring

![Webinterface](http://shares.lukaslueck.de/api/cloud/1/drive/lukas-lueck.clouddrive.lukaslueck.de/sharedLinks/id/915dfca3-f2b4-4d1e-b276-d94459ea18c8/data/Screenshot.png)

## Use case scenario
This software is ideal to watch the temperature at many different points in your house, in a greenhouse, in a server, etc. It shows you clear data, is easy to install, is easy to extend and you can modify it as much as you want. 
## Features
* Cyclical temperature monitoring
* Webinterface
* Graphical presantation
* Renamable sensor names
* Hardware start, stop button (not necessary)
* etc.

## Used hardware
Raspberry Pi 2, some wires, some resistors and a 1-wire temperature sensor [DS18B20](http://www.amazon.de/DS18B20-Digital-Temperature-Sensor-Thermperatursensor/dp/B00BJY8S8C)
## Wiring
* http://www.it-hellmann.de/wp-content/uploads/2015/07/steckbrett.png
* http://www.peatonet.com/wp/wp-content/uploads/2014/08/PinoutRaspberry-1.jpeg
* http://www.reuk.co.uk/OtherImages/connect-multiple-ds18b2-i2c-sensors-raspberry-pi.jpg

![Wiring](http://shares.lukaslueck.de/api/cloud/1/drive/lukas-lueck.clouddrive.lukaslueck.de/sharedLinks/id/3d8b23fb-63e3-4b1e-9765-cf1a188fc6c0/data/IMG_20150930_140614.jpg?width=800&height=800)

## General Setup
First of all you need to install a distribution on your Raspberry Pi. The distribution I used and this software was tested on was Hypriot OS, but feel free to download and test any other distribution and write a short post if that works aswell. When you're finished, you can continue on the command line (with sudo privileges):
````
apt-get update
apt-get upgrade
apt-get install nginx php5-fpm php5-cli git-core build-essential
git clone git://git.drogon.net/wiringPi
cd wiringPi
git pull origin
./build
cd
````
At this step you should download this Github folder and place it to `/var/www`. Then replace `/etc/nginx` with `/var/www/temperature-monitoring/nginx` to have the configuration of nginx. Now disable the default server and enable our new server:
````
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/server.conf /etc/nginx/sites-enabled/server
service nginx start
````
Download and unzip the following files and place them in /var/www
* https://codeload.github.com/IronSummitMedia/startbootstrap-4-col-portfolio/zip/v1.0.3 and rename it to "bootstrap".
* https://codeload.github.com/angularjs-de/angularjs-tutorial-code/zip/gh-pages and rename it to "angularjs".
* https://codeload.github.com/masayuki0812/c3/zip/0.4.10 and rename it to "c3".
* https://codeload.github.com/mbostock/d3/zip/master and rename it to "d3".
* https://code.angularjs.org/1.4.3/angular-1.4.3.zip 

To install Slim Framework we're going to use the command line again.
````php
cd /var/www
curl -sS https://getcomposer.org/installer | php
php composer.phar require slim/slim
````
For permission reasons you have to execute the following script by doing:
````
sh /var/www/temperature-monitoring/temperatureEvaluation/firststart.sh
````
In the last step we have to define crontab. To do so:
````
crontab -e
````
And add these lines to the end of the file:
````
*/15    *       *       *       *       python /var/www/temperature-monitoring/temperatureEvaluation/activeTrueFalse.py
@reboot sudo sh /var/www/temperature-monitoring/temperatureEvaluation/start.sh
@reboot sudo python /var/www/temperature-monitoring/temperatureEvaluation/checkHardwareButton.py
@reboot sudo python /var/www/temperature-monitoring/temperatureEvaluation/writeSensorNames.py
````

## Future?
* Easy way to change cycle duration?
* Save data on an external USB stick?
* Use some database to see min, max, etc. temperature (InfluxDB?)?
* Create some kind of hardware to sell this software as a product?

If you are able to and want to add some of these features, feel free to do it.
