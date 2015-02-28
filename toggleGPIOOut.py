#!/usr/bin/python

import RPi.GPIO as GPIO
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-o", "--gpioout", action="store", type="int", dest="gpioout", default=4, help="GPIO number where OUTPUT device is connected")
(options, args) = parser.parse_args()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(options.gpioout, GPIO.OUT)
if GPIO.input(options.gpioout):
	print 'Turning gpio {} OFF'.format(options.gpioout)
	GPIO.output(options.gpioout,False)
else:
	print 'Turning gpio {} ON'.format(options.gpioout)
	GPIO.output(options.gpioout,True)
