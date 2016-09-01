#!/bin/sh
set -x #echo on

sleep 120

date | tee /home/pi/CAPLink/dt.log

cd /home/pi/CAPLink

chmod +x release/startscript.sh
./release/startscript.sh 2>&1 | tee  /home/pi/CAPLink/start.log
