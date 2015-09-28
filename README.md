# temperature-monitoring

## Use case scenario
## Features
## Used hardware
## General Setup
First of all you need to install a distribution on your Raspberry Pi. The distribution I used and this software was tested was Hypriot OS, but feel free to download and test another distribution and write a short post if that works aswell. When you're finished, you can continue on the command line (with sudo privileges):
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
Now we're going to replace some files. First of all replace the nginx.conf and the server.conf

You can find these files in the folder /etc

Now disable the default server and enable our new server:
````php
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/server.conf /etc/nginx/sites-enabled/server
service nginx start
````

## Future?
