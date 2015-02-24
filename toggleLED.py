#!/usr/bin/python

import RPi.GPIO as GPIO
import time

led = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
if GPIO.input(led):
	print 'Turning LED OFF'
	GPIO.output(led,False)
else:
	print 'Turning LED ON'
	GPIO.output(led,True)
