#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--gpioin", action="store", type="int", dest="gpioin", default=4, help="GPIO number where INPUT device is connected")
(options, args) = parser.parse_args()

GPIO.setmode(GPIO.BCM)
def logInputOff(channel):
	print('Input turned OFF')

GPIO.setup(options.gpioin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(options.gpioin, GPIO.FALLING, callback=logInputOff)
i = 0
while True:
	i = i + 1
	print(i)
	time.sleep(1)
GPIO.cleanup()
