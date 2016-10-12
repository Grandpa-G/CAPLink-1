#!/bin/sh
set -x #echo on

echo "update start"

echo "clear git lock"
rm .git/*.lock
echo "cleared"

echo "$1"
MUMBLE='mumble:'
CAPLINK='/home/pi/CAPLink'

SERIAL="$(cat /proc/cpuinfo | grep Serial | cut -d ':' -f 2)"
SERIAL="$(echo "${SERIAL}" | sed -e 's/^[[:space:]]*//')"

echo "serial number"
echo $SERIAL >> serial.log
 
cd $CAPLINK
#send the serial.log even though it might get overwritten below
echo "send mm.log"
curl -T serial.log -u caplink:mumble ftp://caplink.azwg.org/CAPLink/$SERIAL/
#echo "send m.log"
#curl -T m.log -u caplink:mumble ftp://caplink.azwg.org/CAPLink/$SERIAL/

cp release/start.sh .
cp release/startscript.sh .
cp release/hourly.sh .

chmod +x *.sh

python cron.py

echo "update done"
