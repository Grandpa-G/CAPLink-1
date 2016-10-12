#!/bin/bash
set -x #echo on

SERIAL="$(cat /proc/cpuinfo | grep Serial | cut -d ':' -f 2)"
SERIAL="$(echo "${SERIAL}" | sed -e 's/^[[:space:]]*//')"

echo "in hourly test"
pwd >hourly.log
date >>hourly.log

sudo netstat -tu >mumbleStat
sudo chown pi:pi mumbleStat
cat mumbleStat >>hourly.log

running=$(grep -ic "64738" mumbleStat)
if [ $running -eq 1 ]
 then
  echo "Mumble running." >> hourly.log
#  curl -T hourly.log -u caplink:mumble ftp://caplink.azwg.org/CAPLink/$SERIAL/
else
  echo "rebooting" >>hourly.log
#  curl -T hourly.log -u caplink:mumble ftp://caplink.azwg.org/CAPLink/$SERIAL/

  sudo reboot
fi



