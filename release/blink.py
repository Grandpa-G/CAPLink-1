#!/usr/bin/env python
# -*- coding: utf-8

import argparse

import RPi.GPIO as GPIO
import time

ledPin=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)

def attention():
    for num in range(0,0):
      GPIO.output(ledPin,1)
      time.sleep(0.025)
      GPIO.output(ledPin,0)
      time.sleep(0.025)

def main():

  attention()

if __name__ == '__main__':
    main()
