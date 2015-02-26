#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--led", action="store", type="int", dest="ledgpio", default=4, help="GPIO number where led is connected")
parser.add_option("-i", "--interval", action="store", type="float", dest="diminterval", default=0.1, help="Time interval for led diming")
parser.add_option("-f", "--frequency", action="store", type="int", dest="frequency", default=50, help="PWM frequency")
parser.add_option("-s", "--step", action="store", type="int", dest="step", default=5, help="PWM change step")
(options, args) = parser.parse_args()

GPIO.setmode(GPIO.BCM)
GPIO.setup(options.ledgpio, GPIO.OUT)

p = GPIO.PWM(options.ledgpio, options.frequency)
p.start(0)
try:
    while 1:
        for dc in range(0, 101, options.step):
            p.ChangeDutyCycle(dc)
            time.sleep(options.diminterval)
        for dc in range(100, -1, options.step*(-1)):
            p.ChangeDutyCycle(dc)
            time.sleep(options.diminterval)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
