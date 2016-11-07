#!/usr/bin/env python
# -*- coding: utf-8

import argparse
import os ,sys
import socket

def internet(host="8.8.8.8", port=53, timeout=3):
#   Host: 8.8.8.8 (google-public-dns-a.google.com)
#   OpenPort: 53/tcp
#   Service: domain (DNS/TCP)

   try:
     socket.setdefaulttimeout(timeout)
     socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
     return True
   except Exception as ex:
     print ex.message
     return False

import RPi.GPIO as GPIO
import time

CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

ledPin=17
PTTPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)

def dot():
	GPIO.output(ledPin,1)
	time.sleep(0.2)
	GPIO.output(ledPin,0)
	time.sleep(0.2)

def dash():
	GPIO.output(ledPin,1)
	time.sleep(0.5)
	GPIO.output(ledPin,0)
	time.sleep(0.2)

def errorDisplay(code):
    for num in range(0,code):
      GPIO.output(ledPin,1)
      time.sleep(0.5)
      GPIO.output(ledPin,0)
      time.sleep(0.2)

    time.sleep(0.5)


def attention():
    for num in range(0,3):
      GPIO.output(ledPin,1)
      time.sleep(0.1)
      GPIO.output(ledPin,0)
      time.sleep(0.1)

def morseCode(text):
    for letter in text:
        for symbol in CODE[letter.upper()]:
          if symbol == '-':
            dash()
          elif symbol == '.':
            dot()
          else:
            time.sleep(0.5)
        time.sleep(0.5)

def main():

  attention()
  time.sleep(5.)

  notConnected = True
  while notConnected:
    if(internet()):
      print 'Connected'
      errorDisplay(2)
#    morseCode('V')
      notConnected = False
    else:
      print 'No connection'
      errorDisplay(5)
#   morseCode('SOS')
      notConnected = True
    time.sleep(1.)
 

if __name__ == '__main__':
    main()
