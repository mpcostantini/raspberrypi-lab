#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-o", "--gpioout", action="store", type="int", dest="gpioout", default=4, help="GPIO number where OUTPUT device is connected")
parser.add_option("-t", "--time", action="store", type="float", dest="blinktime", default=0.5, help="Time interval for blinking")
(options, args) = parser.parse_args()

offtime = 0.1
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(options.gpioout, GPIO.OUT)
while True:
	print 'Turning gpio {} ON'.format(options.gpioout)
	GPIO.output(options.gpioout,True)
	time.sleep(offtime)
	print 'Turning gpio {} OFF for {} seconds'.format(options.gpioout, options.blinktime)
	GPIO.output(options.gpioout,False)
	time.sleep(options.blinktime)
GPIO.cleanup()
