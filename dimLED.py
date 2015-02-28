#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-o", "--gpioout", action="store", type="int", dest="gpioout", default=4, help="GPIO number where OUTPUT device is connected")
parser.add_option("-t", "--time", action="store", type="float", dest="dimtime", default=0.1, help="Time interval for diming")
parser.add_option("-f", "--frequency", action="store", type="int", dest="frequency", default=50, help="PWM frequency")
parser.add_option("-s", "--step", action="store", type="int", dest="step", default=5, help="PWM change step")
(options, args) = parser.parse_args()

GPIO.setmode(GPIO.BCM)
GPIO.setup(options.gpioout, GPIO.OUT)

p = GPIO.PWM(options.gpioout, options.frequency)
p.start(0)
try:
    while 1:
    	print 'Diming gpio {} to ON'.format(options.gpioout)
        for dc in range(0, 101, options.step):
            p.ChangeDutyCycle(dc)
            time.sleep(options.dimtime)
        print 'Diming gpio {} to OFF'.format(options.gpioout)
        for dc in range(100, -1, options.step*(-1)):
            p.ChangeDutyCycle(dc)
            time.sleep(options.dimtime)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
