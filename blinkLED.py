#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--led", action="store", type="int", dest="ledgpio", default=4, help="GPIO number where led is connected")
parser.add_option("-i", "--interval", action="store", type="float", dest="blinkinterval", default=0.5, help="Time interval for led blinking")
(options, args) = parser.parse_args()

offtime = 0.1
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(options.ledgpio, GPIO.OUT)
while True:
	GPIO.output(options.ledgpio,True)
	time.sleep(offtime)
	GPIO.output(options.ledgpio,False)
	time.sleep(options.blinkinterval)

