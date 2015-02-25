#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--led", action="store", type="int", dest="ledgpio", default=4, help="GPIO number where led is connected")
(options, args) = parser.parse_args()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(options.ledgpio, GPIO.OUT)
if GPIO.input(options.ledgpio):
	print 'Turning led in gpio {} OFF'.format(options.ledgpio)
	GPIO.output(options.ledgpio,False)
else:
	print 'Turning led in gpio {} ON'.format(options.ledgpio)
	GPIO.output(options.ledgpio,True)

